#version 330 core
in vec2 texCoords;
in vec3 fragPos;
in vec3 fragNormal;

out vec4 fragColor;

struct Attenuation {
  float constant;
  float linear;
  float quadratic;
};

struct Material {
  sampler2D diffuse;
  sampler2D specular;
  sampler2D emission;
  float shininess;

  Attenuation emissionAttenuation;
};

struct DirectionalLight {
  vec3 direction;

  vec3 ambient;
  vec3 diffuse;
  vec3 specular;
};

struct PointLight {
  vec3 position;

  vec3 ambient;
  vec3 diffuse;
  vec3 specular;

  Attenuation attenuation;
};

uniform float time;
uniform Material material;

#define NUM_DIRECTIONAL_LIGHTS 1
uniform DirectionalLight directionalLights[NUM_DIRECTIONAL_LIGHTS];

#define NUM_POINT_LIGHTS 1
uniform PointLight pointLights[NUM_POINT_LIGHTS];

/**
 * Calculate the Phong shading model with ambient, diffuse, and specular
 * components. Does not include attenuation.
 */
vec3 shadePhong(Material material, vec3 lightAmbient, vec3 lightDiffuse,
                vec3 lightSpecular, vec3 lightDir, vec3 viewDir, vec3 normal,
                vec2 texCoords) {
  vec3 diffuseMap = vec3(texture(material.diffuse, texCoords));

  // Ambient.
  vec3 ambient = lightAmbient * diffuseMap;

  // Diffuse.
  float diffuseIntensity = max(dot(normal, lightDir), 0.0);
  vec3 diffuse = lightDiffuse * (diffuseIntensity * diffuseMap);

  // Specular.
  vec3 specularMap = vec3(texture(material.specular, texCoords));
  vec3 reflectDir = reflect(-lightDir, normal);
  float specularIntensity =
      pow(max(dot(viewDir, reflectDir), 0.0), material.shininess);
  vec3 specular = lightSpecular * (specularIntensity * specularMap);

  // Combine components.
  return ambient + diffuse + specular;
}

/**
 * Calculate attenuation based on fragment distance from a light source.
 * Returns a multipler that can be used in shading.
 */
float calcAttenuation(Attenuation attenuation, float fragDist) {
  return 1.0 / (attenuation.constant + attenuation.linear * fragDist +
                attenuation.quadratic * (fragDist * fragDist));
}

vec3 shadeDirectionalLight(Material material, DirectionalLight light,
                           vec3 fragPos, vec3 normal, vec2 texCoords) {
  vec3 lightDir = normalize(-light.direction);
  vec3 viewDir = normalize(-fragPos);

  return shadePhong(material, light.ambient, light.diffuse, light.specular,
                    lightDir, viewDir, normal, texCoords);
}

vec3 shadePointLight(Material material, PointLight light, vec3 fragPos,
                     vec3 normal, vec2 texCoords) {
  vec3 lightDir = normalize(light.position - fragPos);
  vec3 viewDir = normalize(-fragPos);

  // Calculate attenuation from point light source.
  float lightDist = length(light.position - fragPos);
  float attenuation = calcAttenuation(light.attenuation, lightDist);

  vec3 result =
      shadePhong(material, light.ambient, light.diffuse, light.specular,
                 lightDir, viewDir, normal, texCoords);
  // Attenuate the phong model.
  return result * attenuation;
}

vec3 shadeEmission(Material material, vec3 fragPos, vec2 texCoords) {
  // Calculate emission attenuation towards camera.
  float fragDist = length(fragPos);
  float attenuation = calcAttenuation(material.emissionAttenuation, fragDist);

  // Emission.
  vec3 emission = vec3(texture(material.emission, texCoords)) * attenuation;

  // Special effect.
  // TODO: Remove.
  return (sin(time * 0.5) * 0.2 + 0.2) * emission;
}

void main() {
  vec3 normal = normalize(fragNormal);

  vec3 result = vec3(0.0);

  // Shade with directional lights.
  for (int i = 0; i < NUM_DIRECTIONAL_LIGHTS; i++) {
    result += shadeDirectionalLight(material, directionalLights[i], fragPos,
                                    normal, texCoords);
  }

  // Shade with point lights.
  for (int i = 0; i < NUM_POINT_LIGHTS; i++) {
    result +=
        shadePointLight(material, pointLights[i], fragPos, normal, texCoords);
  }

  // Add emissions.
  result += shadeEmission(material, fragPos, texCoords);

  fragColor = vec4(result, 1.0);
}
