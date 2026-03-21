import numpy as np

# Sample data: (x, y, z)
points = np.array([
    [1.0, 2.0, 5.0],
    [3.0, 4.0, 1.0],
    [5.0, 6.0, 5.0],
    [7.0, 8.0, 2.0]
])

target_z = 5.0

# 1. Using Boolean Indexing (Fastest)
mask = points[:, 2] == target_z
result = points[mask]


print(result)
indices = np.where(points[:, 2] == 5.0)
result = points[np.isclose(points[:, 2], target_z)]