import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Khởi tạo Pygame
pygame.init()
viewport = (800, 600)
pygame.display.set_mode(viewport, DOUBLEBUF | OPENGL)

# Cài đặt các thông số cho OpenGL
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (viewport[0] / viewport[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Góc quay của cube
angle = 0

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Di chuyển và xoay cube
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(angle, 0, 1, 0)  # Xoay quanh trục y

    # Xác định các đỉnh của cube
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    # Xác định các mặt của cube
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

    # Cập nhật góc quay của cube
    angle += 1
