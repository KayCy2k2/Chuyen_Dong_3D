import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

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

# Góc quay của sphere theo các trục x, y, z
angles = [0, 0, 0]

# Tốc độ quay của sphere
rotation_speed = 1

# Tọa độ điểm trung tâm quay
rotation_center = [0.0, 0.0, 0.0]

# Bán kính của sphere
radius = 1.0

# Số lượng lưới tạo thành sphere
num_segments = 30

# Hàm vẽ sphere
def draw_sphere():
    for i in range(num_segments):
        lat0 = math.pi * (-0.5 + float(i - 1) / num_segments)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i) / num_segments)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        # Hình thành các đường kỹ thuật số của sphere
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            lng = 2 * math.pi * float(j - 1) / num_segments
            x = math.cos(lng)
            y = math.sin(lng)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
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
                radius -= 0.1  # Giảm bán kính
            elif event.key == pygame.K_DOWN:
                radius += 0.1  # Tăng bán kính
            elif event.key == pygame.K_LEFT:
                num_segments -= 5  # Giảm số lượng lưới
                if num_segments < 5:
                    num_segments = 5
            elif event.key == pygame.K_RIGHT:
                num_segments += 5  # Tăng số lượng lưới

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Di chuyển và xoay toàn bộ hệ tọa độ
    glTranslatef(0, 0, -radius)
    glRotatef(angles[0], 1, 0, 0)  # Xoay quanh trục x
    glRotatef(angles[1], 0, 1, 0)  # Xoay quanh trục y
    glRotatef(angles[2], 0, 0, 1)  # Xoay quanh trục z
    glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])

    # Vẽ sphere
    draw_sphere()

    pygame.display.flip()
    pygame.time.wait(10)

    # Cập nhật góc quay của sphere
    angles = [(angle + rotation_speed) % 360 for angle in angles]

pygame.quit()
