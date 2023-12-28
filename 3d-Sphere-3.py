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

# Góc quay của khối cầu thứ nhất theo các trục x, y, z
angles1 = [1, 0, 0]

# Tốc độ quay của khối cầu thứ nhất
rotation_speed1 = 1

# Tọa độ điểm trung tâm quay của khối cầu thứ nhất
rotation_center1 = [0.0, 0.0, 0.0]

# Khoảng cách từ tâm đến điểm trung tâm quay của khối cầu thứ nhất
distance_from_center1 = 5.0

# Góc quay của khối cầu thứ hai theo các trục x, y, z
angles2 = [0, 1, 0]

# Tốc độ quay của khối cầu thứ hai
rotation_speed2 = 1

# Tọa độ điểm trung tâm quay của khối cầu thứ hai
rotation_center2 = [0.0, 0.0, 0.0]

# Khoảng cách từ tâm khối cầu thứ nhất đến tâm khối cầu thứ hai
distance_between_spheres = 3.0

# Vẽ khối cầu dạng lưới
def draw_sphere(radius=1, slices=16, stacks=16):
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

        # Xử lý sự kiện bàn phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                distance_from_center1 -= 0.5  # Giảm khoảng cách từ tâm khối cầu thứ nhất
            elif event.key == pygame.K_DOWN:
                distance_from_center1 += 0.5  # Tăng khoảng cách từ tâm khối cầu thứ nhất

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Di chuyển và xoay toàn bộ hệ tọa độ cho khối cầu thứ nhất
    glTranslatef(0, 0, -distance_from_center1)
    glRotatef(angles1[0], 1, 0, 0)  # Xoay quanh trục x
    glRotatef(angles1[1], 0, 1, 0)  # Xoay quanh trục y
    glRotatef(angles1[2], 0, 0, 1)  # Xoay quanh trục z

    # Vẽ khối cầu thứ nhất
    draw_sphere()

    # Di chuyển và xoay toàn bộ hệ tọa độ cho khối cầu thứ hai
    glTranslatef(distance_between_spheres, 0, 0)
    glRotatef(angles2[0], 1, 0, 0)  # Xoay quanh trục x
    glRotatef(angles2[1], 0, 1, 0)  # Xoay quanh trục y
    glRotatef(angles2[2], 0, 0, 1)  # Xoay quanh trục z
    glTranslatef(-rotation_center2[0], -rotation_center2[1], -rotation_center2[2])

    # Vẽ khối cầu thứ hai
    draw_sphere()

    pygame.display.flip()

    angles1 = [(angle + rotation_speed1) % 360 for angle in angles1]
    angles2 = [(angle + rotation_speed2) % 360 for angle in angles2]

pygame.quit()
