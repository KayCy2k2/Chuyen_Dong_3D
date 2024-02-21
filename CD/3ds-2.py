from OpenGL.GLUT import *

def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # Màu đỏ cho trục x
    glVertex3f(-2.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)

    # Vẽ ký hiệu góc tọa độ x
    glRasterPos3f(2.2, 0.0, 0.0)
    glutBitmapString(GLUT_BITMAP_HELVETICA_10, "x")

    glColor3f(0.0, 1.0, 0.0)  # Màu xanh lá cho trục y
    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)

    # Vẽ ký hiệu góc tọa độ y
    glRasterPos3f(0.0, 2.2, 0.0)
    glutBitmapString(GLUT_BITMAP_HELVETICA_10, "y")

    glColor3f(0.0, 0.0, 1.0)  # Màu xanh dương cho trục z
    glVertex3f(0.0, 0.0, -2.0)
    glVertex3f(0.0, 0.0, 2.0)

    # Vẽ ký hiệu góc tọa độ z
    glRasterPos3f(0.0, 0.0, 2.2)
    glutBitmapString(GLUT_BITMAP_HELVETICA_10, "z")
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow("Hệ tọa độ 3 chiều")
glutDisplayFunc(draw_axes)
glutMainLoop()
