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

# Góc quay của pyramid theo các trục x, y, z
angles = [0, 0, 0]

# Tốc độ quay của pyramid
rotation_speed = 1

# Tọa độ điểm trung tâm quay
rotation_center = [0.0, 0.0, 0.0]

# Khoảng cách từ tâm pyramid đến điểm trung tâm quay
distance_from_center = 5

# Hàm vẽ pyramid
def draw_pyramid():
    # Xác định các đỉnh của pyramid
    vertices = (
        (0, 1, 0),  # Đỉnh đỉnh
        (-1, -1, 1),  # Đỉnh dưới bên trái
        (1, -1, 1),  # Đỉnh dưới bên phải
        (1, -1, -1),  # Đỉnh dưới sau bên phải
        (-1, -1, -1)  # Đỉnh dưới sau bên trái
    )

    # Xác định các mặt của pyramid
    edges = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 1)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Xử lý sự kiện bàn phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                distance_from_center -= 0.5  # Giảm khoảng cách từ tâm
            elif event.key == pygame.K_DOWN:
                distance_from_center += 0.5  # Tăng khoảng cách từ tâm

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Di chuyển và xoay toàn bộ hệ tọa độ
    glTranslatef(0, 0, -distance_from_center)
    glRotatef(angles[0], 1, 0, 0)  # Xoay quanh trục x
    glRotatef(angles[1], 0, 1, 0)  # Xoay quanh trục y
    glRotatef(angles[2], 0, 0, 1)  # Xoay quanh trục z
    glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])

    # Vẽ pyramid
    draw_pyramid()

    pygame.display.flip()
    pygame.time.wait(10)

    # Cập nhật góc quay của pyramid
    angles = [(angle + rotation_speed) % 360 for angle in angles]

pygame.quit()
