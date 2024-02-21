import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
# Khởi tạo pygame và OpenGL
pygame.init()
display = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
glEnable(GL_DEPTH_TEST)

# Định nghĩa các biến
vertices = [
    (0.0, 0.0, 0.0),
    (0.5, 0.0, 0.0),
    (0.5, 0.5, 0.0),
    (0.0, 0.5, 0.0),
    (0.0, 0.0, 1.0),
    (0.5, 0.0, 1.0),
    (0.5, 0.5, 1.0),
    (0.0, 0.5, 1.0),
]
colors = [
    (0.0, 0.0, 0.0),
    (0.5, 0.0, 0.0),
    (0.5, 0.5, 0.0),
    (0.0, 0.5, 0.0),
    (0.0, 0.0, 1.0),
    (0.5, 0.0, 1.0),
    (0.5, 0.5, 1.0),
    (0.0, 0.5, 1.0),
]

# Vẽ hình lá
def draw_leaf():
    glBegin(GL_TRIANGLES)
    for i in range(len(vertices)):
        glColor3f(*colors[i])
        glVertex3f(*vertices[i])
    glEnd()

# Vòng lặp chính
while True:
    # Vẽ hình lá
    draw_leaf()

    # Cập nhật màn hình
    pygame.display.flip()

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
