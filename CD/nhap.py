
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Khởi tạo pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Khởi tạo OpenGL
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Xóa màn hình
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Màn hình vẽ hình - ở đây vẽ một hình tam giác
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -6.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()

    # Màn hình nền xanh hiển thị chữ
    glLoadIdentity()
    glTranslatef(1.5, 0.0, -6.0)
    glColor3f(0.0, 1.0, 0.0)
    glScalef(0.5, 0.5, 0.5)
    message = "Hello, GPTGO!"
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 32)
    text_surface = font.render(message, True, (0, 255, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos2d(-1, -1)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    pygame.display.flip()
    pygame.time.wait(10)

