import numpy as np
from polar_convert import *
from stl import mesh

file = "cube.stl"
data = mesh.Mesh.from_file(file)
N = len(data)
x = data.x
y = data.y
z = data.z

# polarize points — shape (N_triangles, 3, 3): [triangle, vertex, r/theta/phi]
r, theta, phi = cartesian_to_spherical(x, y, z)
polarized = np.stack([r, theta, phi], axis=-1)

# filter by phi — phi in [0, pi]: 0 = +z, pi = -z, pi/2 = horizontal
phi_vals = polarized[:, :, 2]
vertical_up_mask   = np.isclose(phi_vals, 0)
vertical_down_mask = np.isclose(phi_vals, np.pi)
horizontal_mask    = np.isclose(phi_vals, np.pi / 2)

vertical_up   = polarized[vertical_up_mask]
vertical_down = polarized[vertical_down_mask]
horizontal    = polarized[horizontal_mask]

print("Vertical up points:",   vertical_up.shape)
print("Vertical down points:", vertical_down.shape)
print("Horizontal points:",    horizontal.shape)

# convert back to cartesian
new_r     = polarized[:, :, 0]
new_theta = polarized[:, :, 1]
new_phi   = polarized[:, :, 2]

new_x, new_y, new_z = spherical_to_cartesian(new_r, new_theta, new_phi)

new_mesh = mesh.Mesh(np.zeros(N, dtype=mesh.Mesh.dtype))
new_mesh.vectors = np.stack([new_x, new_y, new_z], axis=-1)
new_mesh.save('output.stl')
