from svgpathtools import svg2paths, wsvg
import math
import numpy as np

def main():
<<<<<<< HEAD
   paths, attributes = properties()
   points = getPoints(attributes)
    # points = [[10, 2], [0, 2], [1, 10], [1, 0]]
   topL,topR,bottomL,bottomR = getVertices(points)
   print(topL,topR,bottomL,bottomR)
   calculate()

def getPoints(attributes):
=======
    paths, attributes = properties()
    print("Got paths and attritbutes")
    print(attributes)
    # points = getPoints(attributes)
    # # points = [[10, 2], [0, 2], [1, 10], [1, 0]]
    # topL,topR,bottomL,bottomR = getVertices(points)
    # with open("vertices.txt", "w") as file:
    #     file.write(f"{topL},{topR},{bottomL},{bottomR}")
    # #    top, left, right, bottom = calculate(topL,topR,bottomL,bottomR)
    # # topL,topR,bottomL,bottomR = [[1152.62,1567.78],[ 11.7154,913.383 ],[1988.28,1088.46],[847.382,432.222]]
    # getAngles(topL,topR,bottomL,bottomR)
    
    #    compare()


def getAngles(topL,topR,bottomL,bottomR):
    topAngle = math.atan((topR[1] - topL[1])/(topR[0] - topL[0]))
    print(f"top angle: {math.degrees(topAngle)}")
    bottomAngle = math.atan((bottomL[1]-bottomR[1])/(bottomL[0]-bottomR[0]))
    print(f"bottom angle: {math.degrees(bottomAngle)}")
    leftAngle = math.atan((bottomL[1]-topL[1])/(bottomL[0]-topL[0]))
    print(f"left angle: {math.degrees(leftAngle)}")
    rightAngle = math.atan((bottomR[1]-topR[1])/(bottomR[0]-topR[0]))
    print(f"right angle: {math.degrees(rightAngle)}")
    with open("new_angles.txt", "w") as output:
        output.write(f"top angle: {math.degrees(topAngle)}\n")
        output.write(f"bottom angle: {math.degrees(bottomAngle)}\n")
        output.write(f"left angle: {math.degrees(leftAngle)}\n")
        output.write(f"right angle: {math.degrees(rightAngle)}\n")

def getPoints(attributes):
    print("Getting points")
>>>>>>> 9c59d54 (transform svg)
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
<<<<<<< HEAD
=======
    print("Returning points")
>>>>>>> 9c59d54 (transform svg)
    return cpoints


def properties():
<<<<<<< HEAD
    return svg2paths('mirrored.svg')
=======
    return svg2paths('rotated.svg')
>>>>>>> 9c59d54 (transform svg)

def lengths(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

<<<<<<< HEAD
def calculate():
=======
def compare():
>>>>>>> 9c59d54 (transform svg)
    topL = (-44.28, 902.56)
    topR = (791.39, 423.24)
    bottomL = (1096.63, 1558.8)
    bottomR = (1932.29, 1077.64)
<<<<<<< HEAD

=======
    top = lengths(topL, topR)
    left = lengths(topL, bottomL)
    right = lengths(topR, bottomR)
    bottom = lengths(bottomR, bottomL)
    print("comparison:")
    print(top, left, right, bottom)
    
def calculate(topL, topR, bottomL, bottomR):
>>>>>>> 9c59d54 (transform svg)
    top = lengths(topL, topR)
    left = lengths(topL, bottomL)
    right = lengths(topR, bottomR)
    bottom = lengths(bottomR, bottomL)

<<<<<<< HEAD
    print(top, left, right, bottom)

def getVertices(points):
    pts = np.array(points)
=======
    return top, left, right, bottom

def getVertices(points):
    print("getting vertices")
    pts = np.array(points)
    print("transformed into numpy array")
>>>>>>> 9c59d54 (transform svg)
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
