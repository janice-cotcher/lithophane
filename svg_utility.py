def create_svg_manual(vertices, filename, width, height):
    """
    Creates an SVG file using a manual path string from a list of vertices.
    """
    if not vertices:
        return

    # Start the path string: Move to the first vertex
    path_data = f"M {vertices[0][0]} {vertices[0][1]} "

    # Add Line commands for subsequent vertices
    for x, y in vertices[1:]:
        path_data += f"L {x} {y} "

    # Close the path
    path_data += "Z"

    # Full SVG content
    svg_content = f"""
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <path d="{path_data}" style="fill:none;stroke:red;stroke-width:2" />
</svg>
    """

    # Write to file
    with open(filename, 'w') as f:
        f.write(svg_content.strip())
    print(f"Created SVG file: {filename}")
