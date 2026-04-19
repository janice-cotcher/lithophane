from stl import mesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


file = "durins_door.stl"

# ls = []
data = mesh.Mesh.from_file(file)
vectors = data.vectors
# for triangle in vectors:
#     for point in triangle:
#         ls.append(point)

# vertices = np.array(ls)
# unique_vertices = np.unique(vertices)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

collection = Poly3DCollection(vectors, alpha=0.5)
collection.set_edgecolor('k')
collection.set_facecolor('cyan')
ax.add_collection3d(collection)

# scale = data.points.flatten()
ax.view_init(0, -90, 0)
# ax.auto_scale_xyz(scale, scale, scale)

plt.savefig("visualize.png")