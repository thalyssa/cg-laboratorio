from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CAMERA_POSITION = [0.0, 0.0, 5.0]
CAMERA_ROTATION = [0.0, 0.0, 0.0]

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    gluLookAt(CAMERA_POSITION[0], CAMERA_POSITION[1], CAMERA_POSITION[2],
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)

    # Renderiza a cena aqui

    glutSwapBuffers()

def idle_display():
    glutPostRedisplay()

def reshape(w, h):
    pass

def keyboard_handle(key, x, y):

    axis = 0.1

    if key == GLUT_KEY_UP:
        CAMERA_POSITION[2] -= axis
    if key == GLUT_KEY_DOWN:
        CAMERA_POSITION[2] += axis
    if key == GLUT_KEY_LEFT:
        CAMERA_POSITION[0] -= axis
    if key == GLUT_KEY_RIGHT:
        CAMERA_POSITION[0] += axis

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
    glutSpecialFunc(keyboard_handle)

    glutMainLoop()

#if __name__ == "__main__":
#    main()