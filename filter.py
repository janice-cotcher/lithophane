from stl import mesh
import numpy as np

file = "durins_door.stl"

data = mesh.Mesh.from_file(file)
vectors = data.vectors

x = vectors[0][:,0]
y = vectors[0][:,1]
z = vectors[0][:,2]
# mask1 = (y >=0 & y < 1.7)
print(np.max(z) - np.min(z))