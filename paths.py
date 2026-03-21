from stl import mesh
import numpy as np

vertices = []
data = mesh.Mesh.from_file('mirrored.stl')
vectors = data.vectors
for triangles in vectors:
    for point in triangles:
        vertices.append(point)

print(vertices[0])