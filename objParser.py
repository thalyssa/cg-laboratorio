# Parser para ler e carregar o arquivo lab_full.obj e .mtl

from OpenGL.GL import *
import os

def OBJparser(self, filename: str) -> list[float]:

    vertices = []

    vertex = [] #v
    textcoords = [] #vt
    normals = [] #vn

    with open(filename, 'r') as file:
        for line in file:
            data = line.split(" ")

            if data[0] == 'v':
                vertex.append(self.read_vertex_data(data))
            elif data[0] == 'vt':
                 textcoords.append(self.read_vt_data(data))
            elif data[0] == 'vn':
                 normals.append(self.read_vn_data(data))
            elif data[0] == 'f':
                self.read_face_data(data, vertex, textcoords, normals, vertices)
    
    return vertices

def read_vertex_datas(self, data: list[str]) -> list[float]:
    
    return [
        float(data[1]),
        float(data[2]),
        float(data[3])
    ]

def read_vt_data(self, data: list[str]) -> list[float]:
    
    return [
        float(data[1]),
        float(data[2])
    ]

def read_vn_data(self, data: list[str]) -> list[float]:
    return [
        float(data[1]),
        float(data[2]),
        float(data[3])
    ]

def read_face_data(self, data: list[str],
                   vertex: list[list[float]],
                   textcoords: list[list[float]],
                   normals: list[list[float]],
                   vertices: list[float]) -> None:
    
    triangleCount = len(data) - 3

    for i in range(triangleCount):
        
        self.makeCorner(data[1], vertex, textcoords, normals, vertices)
        self.makeCorner(data[2 + i], vertex, textcoords, normals, vertices)
        self.makeCorner(data[3 + i], vertex, textcoords, normals, vertices)

def makeCorner(self, corner_data: str,
                   vertex: list[list[float]],
                   textcoords: list[list[float]],
                   normals: list[list[float]],
                   vertices: list[float]) -> None:
    
    #v, vt, vn
    corner_triplet = corner_data.split("/")

    for element in vertex[int(corner_triplet[0]) - 1]:
        vertices.append(element)
    for element in textcoords[int(corner_triplet[1]) - 1]:
        vertices.append(element)
    for element in normals[int(corner_triplet[2]) - 1]:
        vertices.append(element)

def MTLparser(filename: str):

    with open(filename, 'r') as file:
        pass