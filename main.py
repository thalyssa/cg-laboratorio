from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame

WINDOW_WIDHT = 1280
WINDOW_HEIGHT = 720

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    draw_triangle()
    glutSwapBuffers()

def idle_display():
    glutPostRedisplay()

def reshape(w, h):
    pass

def keyboard_handle(key, x, y):

    if key == "w":
        pass
    if key == "a":
        pass
    if key == "s":
        pass
    if key == "d":
        pass

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Sistemas de Controle")

    init()

    glutDisplayFunc(display)
    glutIdleFunc(idle_display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard_handle)

    glutMainLoop()

if __name__ == "__main__":
    main()