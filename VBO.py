from OpenGL.GL import *


class VBO:
    def __init__(self):
        self.vbo = glGenBuffers(1)
        self.component_count = 0
        self.vertex_count = 0

    def delete(self):
        glDeleteBuffers(1, [self.vbo])

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

    def unbind(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def set_vertex_attribute(self, component_count, bytelength, data):
        self.component_count = component_count
        stride = 4 * self.component_count
        self.vertex_count = bytelength // stride
        self.bind()
        glBufferData(GL_ARRAY_BUFFER, bytelength, data, GL_STATIC_DRAW)

    def set_slot(self, slot, count, offset=ctypes.c_void_p(0)):
        self.bind()
        glEnableVertexAttribArray(slot)
        glVertexAttribPointer(slot, count, GL_FLOAT, GL_FALSE, 0, offset)

    def draw(self):
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)
