import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()                                               # Khởi tạo Pygame
viewport = (1350, 650)                                      # Thiết lập kích thước cửa sổ
pygame.display.set_mode(viewport, DOUBLEBUF | OPENGL)       # Tạo cửa sổ OpenGL
pygame.display.set_caption("Snake")

glClearColor(1.0, 1.0, 1.0, 1.0)                            # Thiết lập màu nền thành màu đen
glEnable(GL_DEPTH_TEST)                                     # Bật chức năng kiểm tra độ sâu
#glEnable(GL_LIGHTING)                                      # Bật ánh sáng
glEnable(GL_LIGHT0)                                         # Bật nguồn sáng thứ nhất
glMatrixMode(GL_PROJECTION)                                 # Chọn ma trận chiếu
glLoadIdentity()                                            # Đặt lại ma trận chiếu
gluPerspective(45, (viewport[0] / viewport[1]), 0.1, 50.0)  # Thiết lập phép chiếu phối cảnh
glMatrixMode(GL_MODELVIEW)                                  # Chọn ma trận mô hình-view

BLACK = (0, 0, 0)

a, b, c = 0, 0, 0
angles = [a, b, c]             # Góc quay của khối cầu theo các trục x, y, z
q, w, s = 1, 0, 0
rotation_center = [q, w, s]    # Tọa độ điểm trung tâm quay
rotation_speed = 1             # Tốc độ quay của khối cầu
distance_from_center = 5.0     # Khoảng cách từ tâm đến điểm trung tâm quay
distance_from_center1 = 0      # Khoảng cách từ tâm sang trái/phải
distance_from_center2 = 0      # Khoảng cách từ tâm đi lên/xuống
radius = 1                     # Bán kính lưới
slices = 16                    # Số lát cắt theo đường kinh tuyến
stacks = 16                    # Số lát cắt theo đường vĩ tuyến
mode = 0
scale_factor = 0.5             # Kích thước nhân với hệ số này
 
# Vẽ khối cầu dạng lưới
def draw_sphere():
    for stack in range(stacks):
        # Tính toán các góc và giá trị sin, cos cho vòng tròn vĩ độ hiện tại
        stack_angle = (stack / stacks) * math.pi
        next_stack_angle = ((stack + 1) / stacks) * math.pi
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)
        
        glBegin(GL_LINE_STRIP)
        for slice in range(slices):
            slice_angle = (slice / slices) * math.pi
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)
            
            glColor3fv((0.0, 0.2, 0.0))
            glVertex3f(x * sin_next_stack * scale_factor, y * sin_next_stack * scale_factor, cos_next_stack)
            glVertex3f(x * sin_stack * scale_factor, y * sin_stack * scale_factor, cos_stack)
        glEnd()

        glBegin(GL_LINES)
        for slice in range(slices):
            # Tính toán tọa độ các điểm trên hai vòng tròn vĩ độ liên tiếp
            slice_angle = (slice / slices) * math.pi
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            # Vẽ đường thẳng nối hai điểm tương ứng trên hai vòng tròn vĩ độ
            glVertex3f(x * sin_stack, y * sin_stack, cos_stack)
            glVertex3f(x * sin_next_stack, y * sin_next_stack, cos_next_stack)
        glEnd()

# Vẽ lưới trục tọa độ
def draw_axes():
    glColor3fv((0.5, 0.2, 0.6))
    glLineWidth(1.0)
    glBegin(GL_LINES)
    for i in range(-200, 200, 1):  # Adjust grid spacing
        glVertex3f(i, -5.0, -200)
        glVertex3f(i, 0, 200)
        glVertex3f(-200, -5.0, i)
        glVertex3f(200, 0, i)
    glEnd()
   
def abc():
    # Di chuyển và xoay toàn bộ hệ tọa độ
    glTranslatef(-distance_from_center2, -distance_from_center1, -distance_from_center)
    glRotatef(angles[0], 1, 0, 0)   # Xoay quanh trục x
    glRotatef(angles[1], 0, 1, 0)   # Xoay quanh trục y
    glRotatef(angles[2], 0, 0, 1)   # Xoay quanh trục z
    glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])
    
    draw_sphere()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Xử lý sự kiện bàn phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                scale_factor *= 1.1  # Tăng kích thước
            elif event.key == pygame.K_y:
                scale_factor /= 1.1  # Giảm kích thước
                
            if event.key == pygame.K_k:
                mode = 0
            elif event.key == pygame.K_v:
                mode = 1
                
            spin_speed = {
                pygame.K_i:  (-0.2,    0,    0),                                # Giảm khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_o:  ( 0.2,    0,    0)
            }
            rotation_speed  += spin_speed.get(event.key, (0, 0, 0))[0]
            
            views = {
                pygame.K_a: (-10,   0,   0),                                    # Giảm khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_b: ( 10,   0,   0),                                    # Tăng khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_c: (  0, -10,   0),                                    # Không thay đổi khoảng cách, giảm tốc độ quay
                pygame.K_d: (  0,  10,   0),                                    # Không thay đổi khoảng cách, tăng tốc độ quay
                pygame.K_f: (  0,   0, -10),                                    # Giảm khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_g: (  0,   0,  10)
            }
            a   += views.get(event.key, (0, 0, 0))[0]
            b   += views.get(event.key, (0, 0, 0))[1]
            c   += views.get(event.key, (0, 0, 0))[2]    
            
            distance = {
                pygame.K_UP:    (-0.1,    0,    0),                             # Giảm khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_DOWN:  ( 0.1,    0,    0),                             # Tăng khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_LEFT:  (   0, -0.1,    0),                             # Không thay đổi khoảng cách, giảm tốc độ quay
                pygame.K_RIGHT: (   0,  0.1,    0),                             # Không thay đổi khoảng cách, tăng tốc độ quay
                pygame.K_p:     (   0,    0, -0.1),                             # Giảm khoảng cách từ tâm, không thay đổi tốc độ quay
                pygame.K_l:     (   0,    0,  0.1)
            }
            distance_from_center  += distance.get(event.key, (0, 0, 0))[0]
            distance_from_center1 += distance.get(event.key, (0, 0, 0))[1]
            distance_from_center2 += distance.get(event.key, (0, 0, 0))[2]    
            
            adjustmentsa = {
                pygame.K_r: (-0.1,  0,  0),                                     # Decrement radius
                pygame.K_e: ( 0.1,  0,  0),                                     # Increment radius
                pygame.K_j: (   0, -1,  0),                                     # Decrement slices
                pygame.K_h: (   0,  1,  0),                                     # Increment slices
                pygame.K_m: (   0,  0, -1),                                     # Decrement stacks
                pygame.K_n: (   0,  0,  1)                                      # Increment stacks
            }
            radius += adjustmentsa.get(event.key, (0, 0, 0))[0]
            slices += adjustmentsa.get(event.key, (0, 0, 0))[1]
            stacks += adjustmentsa.get(event.key, (0, 0, 0))[2]
                
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Di chuyển và xoay toàn bộ hệ tọa độ
    glTranslatef(-distance_from_center2, -distance_from_center1, -distance_from_center)
    glRotatef(angles[0], 1, 0, 0)   # Xoay quanh trục x
    glRotatef(angles[1], 0, 1, 0)   # Xoay quanh trục y
    glRotatef(angles[2], 0, 0, 1)   # Xoay quanh trục z
    #glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])
        
    draw_sphere()   # Vẽ khối cầu dạng lưới
    
    # Cập nhật góc quay của khối cầu
    if mode == 0:
        angles = [(angle + rotation_speed) % 360 for angle in angles]
    else:
        angles = [a, b, c]
        draw_axes()
    
    pygame.display.flip()
    pygame.time.wait(10)    
pygame.quit()
