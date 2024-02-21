from OpenGL.GL import *
from OpenGL.GLUT import *
from math import pi 
from math import sin
from math import cos

def initGL(width, height):
   glClearColor(0.529, 0.529, 0.529, 0.0)
   glMatrixMode(GL_PROJECTION)

def dibujarCirculo():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.0, 0.0, 0.0)

  glBegin(GL_POLYGON)
  for i in range(400):
    x = 0.25*sin(i) #Cordenadas polares x = r*sin(t) donde r = radio/2  (Circunferencia centrada en el origen)
    y = 0.25*cos(i) #Cordenadas polares y = r*cos(t)
    glVertex2f(x, y)            
  glEnd()
  glFlush()

def keyPressed(*args):
  key = args[0]
  if key == "r":
    glColor3f(1.0, 0.0, 0.0)
  elif key == "g":
    glColor3f(0.0, 1.0, 0.0)
  elif key ==   "b":
    glColor3f(0.0, 0.0, 1.0)
        

def main():
  global window
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(200,200)

  #creando la ventana
  window = glutCreateWindow("Taller uno")

  glutDisplayFunc(dibujarCirculo)
  glutIdleFunc(dibujarCirculo)
  glutKeyboardFunc(keyPressed)
  initGL(500,500)
  glutMainLoop()

if __name__ == "__main__":
  main()