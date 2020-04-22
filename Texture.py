import glm
import numpy as np
from OpenGL.GL import *
from PIL import Image


class Texture:
    def __init__(self, size=256):
        self.cloud_texture = glGenTextures(1)
        self.matrix = np.zeros((size, size), np.uint8)
        self.size = size

        self.source = None

    def create_perlin(self, a=4, b=2):
        xFactor = 1 / (self.size - 1)
        yFactor = 1 / (self.size - 1)

        for i in range(self.size):
            for j in range(self.size):
                x = xFactor * i
                y = yFactor * j

                sum = 0
                res = 0
                freq = a
                scale = b

                for k in range(4):
                    pt = glm.vec2(x * freq, y * freq)
                    val = glm.perlin(pt, glm.vec2(freq)) / scale

                    sum += val
                    res = (sum + 1) / 2

                    freq *= 2
                    scale *= b

                self.matrix[i][j] = res * 255.

        self.source = Image.fromarray(self.matrix).convert("RGB").tobytes("raw", "RGB")
        self.update()

    def shift(self, shift, axis):
        self.matrix = np.roll(self.matrix, shift, axis)
        self.source = Image.fromarray(self.matrix).convert("RGB").tobytes("raw", "RGB")

    def update(self):
        self.bind()

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.size, self.size, 0, GL_RGB, GL_UNSIGNED_BYTE, self.source)

        glGenerateMipmap(GL_TEXTURE_2D)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.cloud_texture)
