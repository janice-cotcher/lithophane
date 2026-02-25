import numpy as np
from stl import mesh

def main():
    # Example usage:
    # Create a cuboid with dimensions 4x6x8 centered at the origin
    vertices = create_cuboid_vertices(4, 6, 8)
    print("Cuboid Vertices (4x6x8):\n", vertices)

    # Create a cuboid with dimensions 2x2x2 centered at (1, 3, 2)
    vertices_offset = create_cuboid_vertices(2, 2, 2, center=(1, 3, 2))
    print("\nCuboid Vertices (2x2x2 centered at (1,3,2)):\n", vertices_offset)

def create_mesh(faces, vertices):
    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]
    # Write the mesh to file "cube.stl"
    cube.save('cube.stl')


def create_cuboid_vertices(length, width, height, center=(0, 0, 0)):
    """
    Generates the vertices of a cuboid from its dimensions.

    Args:
        length (float): The length of the cuboid along the x-axis.
        width (float): The width of the cuboid along the y-axis.
        height (float): The height of the cuboid along the z-axis.
        center (tuple): The (x, y, z) coordinates of the cuboid's center.

    Returns:
        np.ndarray: A NumPy array of shape (8, 3) containing the 8 vertices.
    """
    # Calculate half dimensions
    half_length = length / 2
    half_width = width / 2
    half_height = height / 2
    
    # Define the offsets from the center for each dimension
    x_offsets = [-half_length, half_length]
    y_offsets = [-half_width, half_width]
    z_offsets = [-half_height, half_height]
    
    # Generate all combinations of offsets using a list comprehension
    # This creates the 8 corner points relative to the origin
    vertices_relative = [
        [x, y, z]
        for x in x_offsets
        for y in y_offsets
        for z in z_offsets
    ]
    
    # Convert to a NumPy array and add the center offset
    vertices = np.array(vertices_relative) + np.array(center)
    
    return vertices


if __name__=="__main__":
    main()
