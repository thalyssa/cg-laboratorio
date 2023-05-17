# Parser para ler e carregar o arquivo lab_full.obj e .mtl

from OpenGL.GL import *
import os

MATERIALS_FILEPATH = ' '
OBJ_FILEPATH = ' '

def MTLparser(filename: str):

    with open(filename, 'r') as file:
        pass

def OBJparser(self, filename: str) -> list[float]:

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
            data = line.split()

            if not data:
                pass
            if data[0] == 'v':
                # Tratamento dos vértices
                pass
            elif data[0] == 'vt':
                pass
            elif data[0] == 'vn':
                #Tratamento das normais
                pass
            elif data[0] == 'f':
                #Tratamento das faces
                pass

            