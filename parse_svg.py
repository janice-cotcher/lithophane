from svgelements import *
import numpy as np
from transform import getVertices, getAngles
import re

def main():
    paths = []
    groups = []
    svg = SVG.parse("rotated.svg")
    elements = svg.elements()

    for element in elements:
        if isinstance(element, Path):
            paths.append(element)
        elif isinstance(element, Group):
            groups.append(element)

    points = []

    for path in paths:
        points.append(path.d())
    #     p1 = path.start
    #     p2 = path.end
    #     if p1 not in points:
    #         points.append(p1)
    #     if p2 not in points:
    #         points.append(p2)
    cpoints = getPoints(points)
    # print(cpoints[0])
    topL,topR,bottomL,bottomR = getVertices(cpoints)
    with open("new_vertices.txt", "w") as file:
        file.write(f"{topL},{topR},{bottomL},{bottomR}")
    getAngles(topL,topR,bottomL,bottomR)

def getPoints(attributes):
    print("Getting points")
    cpoints = []
    for item in attributes:
        points = item.split()
        temp1 = points[1].split(',')
        temp2 = points[3].split(',')
        point1 = [float(temp1[0]), float(temp1[1])]
        point2 = [float(temp2[0]), float(temp2[1])]
        if point1 not in cpoints:
            cpoints.append(point1)
        if point2 not in cpoints:
            cpoints.append(point2)
    print("Returning points")
    return cpoints

main()