import pygame as pg
from OpenGL.GL import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
MATERIALS_FILEPATH = ' '
OBJ_FILEPATH = ' '

class App:

    def __init__(self):

        pg.init()
        pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()

        glClearColor(0.1, 0.2, 0.0, 1.0)

        self.mainLoop()

    def mainLoop(self):

        is_running = True

        while(is_running):
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    is_running = False
            
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()
        
        self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    myLab = App()