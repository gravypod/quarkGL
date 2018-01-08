#ifndef QUARKGL_WINDOW_H_
#define QUARKGL_WINDOW_H_

#include <functional>

// Must precede glfw/glad, to include OpenGL functions.
#include <qrk/core.h>

#include <GLFW/glfw3.h>
#include <glad/glad.h>
#include <glm/glm.hpp>

#include <qrk/shared.h>

namespace qrk {

class WindowException : public QuarkException {
  using QuarkException::QuarkException;
};

constexpr int DEFAULT_WIDTH = 800;
constexpr int DEFAULT_HEIGHT = 600;
constexpr char const* DEFAULT_TITLE = "quarkGL";

struct ScreenSize {
  int width;
  int height;
};

class Window {
 private:
  GLFWwindow* window_;
  bool depthTestEnabled_ = false;
  bool stencilTestEnabled_ = false;
  bool blendingEnabled_ = false;

  float lastTime_ = 0.0f;
  float deltaTime_ = 0.0f;
  glm::vec4 clearColor_ = DEFAULT_CLEAR_COLOR;

 public:
  Window(int width = DEFAULT_WIDTH, int height = DEFAULT_HEIGHT,
         const char* title = DEFAULT_TITLE, bool fullscreen = false);
  ~Window();
  GLFWwindow* getGlfwRef() { return window_; }

  void activate();

  // TODO: Consider extracting depth test logic.
  void enableDepthTest() {
    glEnable(GL_DEPTH_TEST);
    depthTestEnabled_ = true;
  }
  void disableDepthTest() {
    glDisable(GL_DEPTH_TEST);
    depthTestEnabled_ = false;
  }

  // TODO: Consider extracting stencil logic out to a separate class.
  void enableStencilTest() {
    glEnable(GL_STENCIL_TEST);
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);
    stencilTestEnabled_ = true;
  }
  void disableStencilTest() {
    glDisable(GL_STENCIL_TEST);
    stencilTestEnabled_ = false;
  }

  void enableStencilUpdates() { glStencilMask(0xFF); }
  void disableStencilUpdates() { glStencilMask(0x00); }

  void stencilAlwaysDraw() { setStencilFunc(GL_ALWAYS); }
  void stencilDrawWhenMatching() { setStencilFunc(GL_EQUAL); }
  void stencilDrawWhenNotMatching() { setStencilFunc(GL_NOTEQUAL); }
  void setStencilFunc(GLenum func) {
    // Set the stencil test to use the given `func` when comparing for fragment
    // liveness.
    glStencilFunc(func, 1, 0xFF);
  }

  // TODO: Consider extracting blending logic.
  void enableBlending() {
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  }
  void disableBlending() { glDisable(GL_BLEND); }

  void enableCulling() { glEnable(GL_CULL_FACE); }
  void disableCulling() { glDisable(GL_CULL_FACE); }

  ScreenSize getSize();
  void setSize(int width, int height);
  glm::vec4 getClearColor() { return clearColor_; }
  void setClearColor(glm::vec4 color) { clearColor_ = color; }

  void makeFullscreen();
  void makeWindowed();

  void loop(std::function<void(float)> callback);

  // TODO: Allow setting window icon.
};
}  // namespace qrk

#endif
