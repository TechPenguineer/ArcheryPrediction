import glfw
from .draw_grid import*
from OpenGL.GL import*
import OpenGL.GL.shaders
from .shader import*


def create_win():
    if not glfw.init():
        return
    window = glfw.create_window(640, 480, "Archery Prediction", None, None)
    if not window:
        glfw.terminate()
        
        return
    glfw.make_context_current(window)
    createShader()
    draw_grid(window)
    while not glfw.window_should_close(window):
        
        glfw.swap_buffers(window)
        glClear(GL_COLOR_BUFFER_BIT) 
        glfw.poll_events()
    glfw.terminate()
    return window
