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

# Góc quay của khối cầu theo các trục x, y, z
angles = [0, 0, 0]

# Tốc độ quay của khối cầu
rotation_speed = 1

# Tọa độ điểm trung tâm quay
rotation_center = [0.0, 0.0, 0.0]

# Vẽ khối cầu dạng lưới
def draw_sphere(radius=1, slices=32, stacks=16):
    for stack in range(stacks):
        stack_angle = (stack / stacks) * math.pi
        next_stack_angle = ((stack + 1) / stacks) * math.pi
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_LINE_STRIP)
        for slice in range(slices + 1):
            slice_angle = (slice / slices) * 2 * math.pi
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            glVertex3f(x * sin_next_stack, y * sin_next_stack, cos_next_stack)
            glVertex3f(x * sin_stack, y * sin_stack, cos_stack)
        glEnd()

        glBegin(GL_LINES)
        for slice in range(slices):
            slice_angle = (slice / slices) * 2 * math.pi
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            glVertex3f(x * sin_stack, y * sin_stack, cos_stack)
            glVertex3f(x * sin_next_stack, y * sin_next_stack, cos_next_stack)
        glEnd()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Di chuyển và xoay toàn bộ hệ tọa độ
    glTranslatef(0, 0, -5.0)
    glRotatef(angles[0], 1, 0, 0)  # Xoay quanh trục x
    glRotatef(angles[1], 0, 1, 0)  # Xoay quanh trục y
    glRotatef(angles[2], 0, 0, 1)  # Xoay quanh trục z

    # Vẽ khối cầu dạng lưới
    draw_sphere()

    pygame.display.flip()
    pygame.time.wait(10)

    # Cập nhật góc quay của khối cầu
    angles = [(angle + rotation_speed) % 360 for angle in angles]

pygame.quit()
