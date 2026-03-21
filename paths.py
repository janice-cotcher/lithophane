from stl import mesh
import numpy as np
from path_utility import find_crease_edges, chain_crease_edges, coords_to_indices
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

ls = []
data = mesh.Mesh.from_file('mirrored.stl')
vectors = data.vectors

for triangle in vectors:
    for point in triangle:
        ls.append(point)

vertices = np.array(ls)
unique_vertices = np.unique(vertices, axis=0)
triangles = coords_to_indices(unique_vertices, vectors)
crease_edges = find_crease_edges(vertices, triangles, target_angle_deg=90.0, tolerance_deg=10)
paths = chain_crease_edges(crease_edges)
for path in paths:
    coord = vertices[path]