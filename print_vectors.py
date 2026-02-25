from stl import mesh
import numpy as np

your_mesh = mesh.Mesh.from_file('surface.stl')

print(your_mesh.vectors.shape)      # dimensions first — good sanity check
print(your_mesh.vectors[0])         # just the first triangle
print(your_mesh.vectors[:5])        # first 5 triangles