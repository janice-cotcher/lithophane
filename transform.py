from svgpathtools import svg2paths, wsvg
import math
import numpy as np

def main():
   paths, attributes = properties()
   points = getPoints(attributes)
    # points = [[10, 2], [0, 2], [1, 10], [1, 0]]
   topL,topR,bottomL,bottomR = getVertices(points)
   print(topL,topR,bottomL,bottomR)
   calculate()

def getPoints(attributes):
    cpoints = []
    for item in attributes:
        points = item['points'].split()
        temp1 = points[0].split(',')
        temp2 = points[1].split(',')
        point1 = [float(temp1[0]), float(temp1[1])]
        point2 = [float(temp2[0]), float(temp2[1])]
        if point1 not in cpoints:
            cpoints.append(point1)
        if point2 not in cpoints:
            cpoints.append(point2)
    return cpoints


def properties():
    return svg2paths('mirrored.svg')

def lengths(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calculate():
    topL = (-44.28, 902.56)
    topR = (791.39, 423.24)
    bottomL = (1096.63, 1558.8)
    bottomR = (1932.29, 1077.64)

    top = lengths(topL, topR)
    left = lengths(topL, bottomL)
    right = lengths(topR, bottomR)
    bottom = lengths(bottomR, bottomL)

    print(top, left, right, bottom)

def getVertices(points):
    pts = np.array(points)
    max = np.argmax(pts, axis=0)
    print("found max")
    bottomL = pts[max[0]]
    print(bottomL)
    topL = pts[max[1]]
    print(topL)
    min = np.argmin(pts, axis=0)
    print("found min")
    bottomR = pts[min[1]]
    print(bottomR)
    topR = pts[min[0]]
    print(topR)
    return topL, topR, bottomL, bottomR

if __name__=="__main__":
    main()
