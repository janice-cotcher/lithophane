import trimesh
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
import pyvista as pv

# load the mesh from the stl file
file='cow.stl'
# file = "durins_door.stl"
# data = mesh.Mesh.from_file(file)
# subdivide the mesh for a more detailed image
mesh = trimesh.load(file)
# Subdivide the entire mesh (simple method)
# This returns new vertices and faces
vertices, faces = trimesh.remesh.subdivide_loop(mesh.vertices, mesh.faces, iterations=2)

# Create a new mesh from the result
# subdivided_mesh = trimesh.Trimesh(vertices=vertices, faces=faces)


# extract all vertices from the mesh triangles and append to a 1D list
# ls = []
# vectors = subdivided.vectors
# for triangle in vectors:
#     for point in triangle:
#         ls.append(point)

vertices = np.array(vertices)
print(vertices.shape)
points = np.unique(vertices, axis=0) # remove duplicate points
plane_origin = points.mean(axis=0) # set the plane origin to centroid of all vertices
plane_normal = np.array([0, 1, 0]) # define viewing direction as XZ
# project 3D space into the XZ plane
new_plane = trimesh.points.project_to_plane(points, plane_normal, plane_origin)

# Plot the 2D projection with no axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(new_plane[:, 0], new_plane[:, 1], s=1, c='black', alpha=0.5)
ax.set_aspect('equal')
ax.axis("off")
plt.tight_layout()
plt.savefig("2Good2cow.png")

# convert the image to black and white

# find the edges of the image

# any hex values greater than 000000 converted to black within the boundaries
