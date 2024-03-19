import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Khởi tạo Pygame
pygame.init()
viewport = (600, 600)
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

# Góc quay của khối cầu theo các trục x, y, z
angles = [1, 0, 0]

# Tốc độ quay của khối cầu
rotation_speed = 1

# Tọa độ điểm trung tâm quay
rotation_center = [0.0, 0.0, 0.0]

# Khoảng cách từ tâm đến điểm trung tâm quay
distance_from_center = 5.0
def draw_circle(radius=1, slices=16, z=0):
    glBegin(GL_LINE_STRIP)
    for slice in range(slices + 1):
        slice_angle = (slice / slices) * 2 * math.pi
        x = radius * math.cos(slice_angle)
        y = radius * math.sin(slice_angle)
        glVertex3f(x, y, z)
    glEnd()

def draw_cone(radius=1, height=1, slices=16):
    glBegin(GL_LINES)
    for slice in range(slices):
        slice_angle = (slice / slices) * 2 * math.pi
        x = radius * math.cos(slice_angle)
        y = radius * math.sin(slice_angle)

        # Vẽ cạnh
        glVertex3f(x, y, 0)
        glVertex3f(0, 0, height)

    glEnd()

    # Vẽ mặt đáy
    draw_circle(radius, slices, 0)
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

    draw_cone()

    pygame.display.flip()
    pygame.time.wait(10)

    # Cập nhật góc quay của khối cầu
    angles = [(angle + rotation_speed) % 360 for angle in angles]

pygame.quit()
