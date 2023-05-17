from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame as pg
import numpy as np

# Classe criada para controlar a visão/câmera em primeira pessoa

class Viewer:

    def __init__(self, position):

        self.position = np.array(position, dtype = np.float32)
        self.theta = 0 # Posição do olhar no plano horizontal
        self.phi = 0 # Posição do olhar no plano vertical
        self.update_vectors()

    
    def update_vectors(self):

        self.forwards = np.array(
            [
                np.cos(np.deg2rad(self.theta)) * np.cos(np.deg2rad(self.phi)),
                np.sin(np.deg2rad(self.theta)) * np.cos(np.deg2rad(self.phi)),
                np.sin(np.deg2rad(self.phi))
            ]
        )

        globalUp = np.array([0,0,1], dtype = np.float32)

        self.right = np.cross(self.forwards, globalUp)
        self.up = np.cross(self.right, self.fowards)