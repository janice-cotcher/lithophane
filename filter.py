from stl import mesh
import numpy as np
from scipy.spatial import cKDTree

file = "durins_door.stl"

data = mesh.Mesh.from_file(file)
vectors = data.vectors
vertices = []
for triangle in vectors:
    for point in triangle:
        if point not in vertices:
            vertices.append(point)

points = np.array(vertices)

# x = data.x
# y = data.y
# z = data.z
# normals = data.normals

