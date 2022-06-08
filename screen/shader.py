import glfw
from .draw_grid import*
from OpenGL.GL import*
import OpenGL.GL.shaders


vertex_shader = """
#version 330
in vec4 position;

void main()
{
    gl_Position=position;
}
""" 

fragment_shader = """
#version 330
void main()
{
    gl_FragColor = vec4(1.0f,0.0f,0.0f,1.0f);
}
"""
def createShader():
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER), 
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))