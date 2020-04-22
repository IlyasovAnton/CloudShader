import ctypes

from EBO import EBO
from Shader import Shader
from Texture import Texture
from VBO import VBO


class Cloud:
    def __init__(self):
        self.positions = [ 1.0,  1.0, 1.0, 1.0,
                           1.0, -1.0, 1.0, 0.0,
                          -1.0, -1.0, 0.0, 0.0,
                          -1.0,  1.0, 0.0, 1.0]

        self.indices = [0, 2, 4, 0, 4, 6]

        self.shader = None
        self.vbo = None
        self.ebo = None
        self.cloud_texture = None

    def delete(self):
        self.shader.delete()
        self.vbo.delete()
        self.ebo.delete()

    def initialize(self):
        self.shader = Shader()

        self.shader.compile(open('shaders/vertex.glsl').read(),
                            open('shaders/fragment.glsl').read())
        self.vbo = VBO()
        self.ebo = EBO()

        self.cloud_texture = Texture(512)
        self.cloud_texture.create_perlin()

        self.vbo.set_vertex_attribute(2, 4 * len(self.positions), (ctypes.c_float * len(self.positions))(*self.positions))
        self.ebo.set_indices(4, 4 * len(self.indices), (ctypes.c_uint * len(self.indices))(*self.indices))

    def draw(self):
        if not self.vbo:
            self.initialize()
        self.shader.use()
        self.vbo.set_slot(0, 2)
        self.vbo.set_slot(1, 2, ctypes.c_void_p(2 * ctypes.sizeof(ctypes.c_float)))
        self.ebo.bind()
        self.ebo.draw()

        self.ebo.unbind()
        self.vbo.unbind()
        self.shader.unuse()
