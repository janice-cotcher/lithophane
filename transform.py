import numpy as np
from polar_convert import cartesian_to_spherical
from stl import mesh

file = "cow.stl"

data = mesh.Mesh.from_file(file)
# vectors = data.vectors
# vertices = []
# for triangle in vectors:
#     for point in triangle:
#         vertices.append(point)


# polarize points
# r, theta, phi = cartesian_to_spherical(x, y, z)

# polarize vectors (v0, v1) (v1, v2) (v2, v0)

# half edge structure


