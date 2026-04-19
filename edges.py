import numpy as np
from stl import mesh

# Load the STL file
your_mesh = mesh.Mesh.from_file('durins_door.stl')

# Each face has 3 vertices (v0, v1, v2)
# We define edges as pairs: (v0, v1), (v1, v2), (v2, v0)
v0 = your_mesh.v0
v1 = your_mesh.v1
v2 = your_mesh.v2

# Stack all edges into a single array
edges = np.vstack([
    np.column_stack([v0, v1]),
    np.column_stack([v1, v2]),
    np.column_stack([v2, v0])
]).reshape(-1, 2, 3)

# To find unique edges, sort the vertex pairs to ensure (A, B) is same as (B, A)
edges_sorted = np.sort(edges, axis=1)

# Reshape to a 2D array of coordinates to use unique()
edges_flat = edges_sorted.reshape(-1, 6)
unique_edges = np.unique(edges_flat, axis=0)

print(f"Total unique edges: {len(unique_edges)}")
