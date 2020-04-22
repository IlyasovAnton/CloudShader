from OpenGL.GL import *


class Shader:
    def __init__(self):
        self.program = glCreateProgram()

    def delete(self):
        glDeleteProgram(self.program)

    def compile(self, vs_src, fs_src):
        vs = self.load(vs_src, GL_VERTEX_SHADER)
        if not vs:
            return
        fs = self.load(fs_src, GL_FRAGMENT_SHADER)
        if not fs:
            return
        glAttachShader(self.program, vs)
        glAttachShader(self.program, fs)
        glLinkProgram(self.program)
        glDeleteShader(vs)
        glDeleteShader(fs)
        if not glGetProgramiv(self.program, GL_LINK_STATUS):
            info = glGetShaderInfoLog(self.program)
            raise Exception(info)

    def load(self, src, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, src)
        glCompileShader(shader)
        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            info = glGetShaderInfoLog(shader)
            glDeleteShader(shader)
            raise Exception(info)
        return shader

    def use(self):
        glUseProgram(self.program)

    def unuse(self):
        glUseProgram(0)
