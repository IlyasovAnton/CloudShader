from OpenGL.GL import *


class EBO:
    def __init__(self):
        self.vbo = glGenBuffers(1)
        self.index_count = 0
        self.index_type = 0

    def delete(self):
        glDeleteBuffers(1, [self.vbo])

    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vbo)

    def unbind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def set_indices(self, stride, bytelength, data):
        self.index_count = bytelength // stride
        self.bind()
        if stride == 1:
            self.index_type = GL_UNSIGNED_BYTE
        elif stride == 2:
            self.index_type = GL_UNSIGNED_SHORT
        elif stride == 4:
            self.index_type = GL_UNSIGNED_INT
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, bytelength, data, GL_STATIC_DRAW)

    def draw(self):
        glDrawElements(GL_TRIANGLES, self.index_count, self.index_type, None)
