from svgelements import *
import numpy as np

paths = []
groups = []
svg = SVG.parse("rotated.svg")
points = []
for element in svg.elements():
    # print(element)
    if isinstance(element, Path):
        # Extract (x, y) from each Point object in the polyline
        # coords = [points.append([pt.x, pt.y]) for pt in element.points()]
        for item in Path:
            print(item)
        
pt_matrix = np.array(points)
print(pt_matrix.shape)