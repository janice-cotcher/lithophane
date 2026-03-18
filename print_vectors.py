from stl import mesh
import numpy as np

data = mesh.Mesh.from_file('moria1.stl')

# Mirror along the X axis (change to y or z depending on which way your lithophane faces)
data.x *= -1

# Flipping inverts the winding order, which reverses the normals
# This fixes them so the faces point the right way again
data.vectors = data.vectors[:, ::-1, :]

data.rotate([0, 0, 1], np.radians(90))

data.save('mirrored.stl')