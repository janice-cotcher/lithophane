from aspose.cad.imageoptions import SvgOptions
from aspose.cad import Image

# Load the STL file
image = Image.load("moria1.stl")

# Create an object of SvgOptions class for SVG export options
svg_options = SvgOptions()

# Convert STL to SVG and save the file
image.save("output.svg", svg_options)

print("Conversion completed successfully!")