import sys
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    # Khởi tạo chương trình OpenGL
    glutInit(sys.argv)
    glutInitWindowSize(640, 480)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("Khối cầu có đổ bóng")

    # Thiết lập các thuộc tính của ánh sáng
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])

    # Thiết lập các thuộc tính của camera
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Tạo một đối tượng GLUquadric để đại diện cho khối cầu
    quad = gluNewQuadric()

    # Thiết lập các thuộc tính của khối cầu
    gluQuadricDrawStyle(quad, GLU_FILL)
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluQuadricTexture(quad, GL_TRUE)

    # Vẽ khối cầu
    gluSphere(quad, 1.0, 100, 100)

    # Vẽ khung nhìn
    glutMainLoop()

if __name__ == "__main__":
    main()