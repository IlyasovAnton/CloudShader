import os

import pygame
from OpenGL.GL import *

from Cloud import Cloud


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_mode((800, 800), pygame.OPENGL | pygame.DOUBLEBUF)

    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

    cloud = Cloud()
    while True:
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            cloud.cloud_texture.shift(-1, 1)
            cloud.cloud_texture.update()
        elif keys[pygame.K_RIGHT]:
            cloud.cloud_texture.shift(1, 1)
            cloud.cloud_texture.update()
        elif keys[pygame.K_UP]:
            cloud.cloud_texture.shift(1, 0)
            cloud.cloud_texture.update()
        elif keys[pygame.K_DOWN]:
            cloud.cloud_texture.shift(-1, 0)
            cloud.cloud_texture.update()

        cloud.draw()

        pygame.display.flip()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                cloud.delete()
                exit()


if __name__ == "__main__":
    main()
