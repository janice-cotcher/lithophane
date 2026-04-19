import trimesh
import numpy as np
import math
mesh = trimesh.load_mesh('durins_door.stl')

all_edges = mesh.edges          # All edges (3 per face)
unique_edges = mesh.edges_unique # Set of unique edges by vertex index
boundary_edges = mesh.outline   # Only edges on the mesh boundary

# print(type(all_edges), type(unique_edges), type(boundary_edges))
# for facet in mesh.facets:
#     mesh.visual.face_colors[facet] = trimesh.visual.random_color()
# mesh.show()
unique, indices = trimesh.grouping.group_distance(all_edges, distance=10)
for index in indices[0]:
    print(all_edges[index])
