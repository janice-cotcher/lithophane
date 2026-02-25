import numpy as np
from stl import mesh

# 1. Create grid
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
xx, yy = np.meshgrid(x, y)
zz = np.sin(xx) * np.cos(yy)  # some function

# 2. Triangulate — each grid square becomes 2 triangles
# For a grid of shape (m, n), we get (m-1)*(n-1)*2 triangles
m, n = xx.shape
triangles = []
for i in range(m - 1):
    for j in range(n - 1):
        # corners of this grid square
        p00 = [xx[i,j],   yy[i,j],   zz[i,j]]
        p10 = [xx[i+1,j], yy[i+1,j], zz[i+1,j]]
        p01 = [xx[i,j+1], yy[i,j+1], zz[i,j+1]]
        p11 = [xx[i+1,j+1], yy[i+1,j+1], zz[i+1,j+1]]
        triangles.append([p00, p10, p01])  # triangle 1
        triangles.append([p10, p11, p01])  # triangle 2

# 3. Build and save the STL
triangles = np.array(triangles)
stl_mesh = mesh.Mesh(np.zeros(len(triangles), dtype=mesh.Mesh.dtype))
for i, tri in enumerate(triangles):
    stl_mesh.vectors[i] = tri

stl_mesh.save('surface.stl')