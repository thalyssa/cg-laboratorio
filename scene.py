from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame as pg
import viewer

class Scene:

    def __init__(self):

        # Carregue todos os materiais da cena aqui

        self.viewer = viewer(position =[0,0,2])

    def update(self, rate):
        pass