#include <qrk/core.h>
#include <qrk/shader.h>
#include <qrk/shader_loader.h>

namespace qrk {

Shader::Shader(const char* vertexPath, const char* fragmentPath) {
  // Read file contents.
  ShaderLoader vertexLoader(vertexPath, ShaderType::VERTEX);
  std::string vertexSourceString = vertexLoader.load();
  ShaderLoader fragmentLoader(fragmentPath, ShaderType::FRAGMENT);
  std::string fragmentSourceString = fragmentLoader.load();

  const char* vertexShaderSource = vertexSourceString.c_str();
  const char* fragmentShaderSource = fragmentSourceString.c_str();

  unsigned int vertexShader, fragmentShader;
  int success;
  char infoLog[512];

  // Compile vertex shader.
  vertexShader = glCreateShader(GL_VERTEX_SHADER);

  glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
  glCompileShader(vertexShader);

  glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(vertexShader, 512, nullptr, infoLog);
    throw ShaderException("ERROR::SHADER::VERTEX::COMPILATION_FAILED\n" +
                          std::string(infoLog));
  }

  // Compile fragment shader.
  fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);

  glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
  glCompileShader(fragmentShader);

  glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(fragmentShader, 512, nullptr, infoLog);
    throw ShaderException("ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n" +
                          std::string(infoLog));
  }

  // Create and link shader program.
  shaderProgram_ = glCreateProgram();

  glAttachShader(shaderProgram_, vertexShader);
  glAttachShader(shaderProgram_, fragmentShader);
  glLinkProgram(shaderProgram_);

  glGetProgramiv(shaderProgram_, GL_LINK_STATUS, &success);
  if (!success) {
    glGetProgramInfoLog(shaderProgram_, 512, nullptr, infoLog);
    throw ShaderException("ERROR::SHADER::LINKING_FAILED\n" +
                          std::string(infoLog));
  }

  // Delete shaders now that they're linked.
  glDeleteShader(vertexShader);
  glDeleteShader(fragmentShader);
}

void Shader::activate() { glUseProgram(shaderProgram_); }
void Shader::deactive() { glUseProgram(0); }

void Shader::addUniformSource(std::shared_ptr<UniformSource> source) {
  uniformSources_.push_back(source);
}

void Shader::updateUniforms() {
  // Update core uniforms.
  setFloat("qrk_time", qrk::time());

  for (auto uniformSource : uniformSources_) {
    uniformSource->updateUniforms(*this);
  }
}

void Shader::setBool(const char* name, bool value) {
  activate();
  glUniform1i(glGetUniformLocation(shaderProgram_, name),
              static_cast<int>(value));
}

void Shader::setInt(const char* name, int value) {
  activate();
  glUniform1i(glGetUniformLocation(shaderProgram_, name), value);
}

void Shader::setFloat(const char* name, float value) {
  activate();
  glUniform1f(glGetUniformLocation(shaderProgram_, name), value);
}

void Shader::setVec3(const char* name, const glm::vec3& vector) {
  activate();
  glUniform3fv(glGetUniformLocation(shaderProgram_, name), 1,
               glm::value_ptr(vector));
}

void Shader::setVec3(const char* name, float v0, float v1, float v2) {
  activate();
  glUniform3f(glGetUniformLocation(shaderProgram_, name), v0, v1, v2);
}

void Shader::setMat4(const char* name, const glm::mat4& matrix) {
  activate();
  glUniformMatrix4fv(glGetUniformLocation(shaderProgram_, name), 1, GL_FALSE,
                     glm::value_ptr(matrix));
}
}  // namespace qrk
