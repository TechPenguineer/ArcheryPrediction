import glfw
from OpenGL.GL import*

def draw_grid(window):
    
    glClearColor(0.2,0.3,0.2,1.0)
    glClear(GL_COLOR_BUFFER_BIT)