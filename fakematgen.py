import sys
import math

def PrintMat(x, transpose):
    if transpose:
        x = map(list,zip(*x))
    s = str(x)
    s = s.replace("[","{")
    s = s.replace("]","}")
    s = s.replace("}, ","}, \n")
    print "float fakeMat[4][4] = "
    print s + ";"


angle = float(sys.argv[1])
axis = sys.argv[2]

xTranslation = 0
yTranslation = 0
zTranslation = 0

if len(sys.argv) >= 6:
    xTranslation = float(sys.argv[3])
    yTranslation = float(sys.argv[4])
    zTranslation = float(sys.argv[5])

transpose = False
if sys.argv[len(sys.argv)-1] == "transpose":
    transpose = True

cosTheta = round(math.cos(angle*math.pi/180.0),4)
sinTheta = round(math.sin(angle*math.pi/180.0),4)

xRot = [
[ 1, 0, 0, xTranslation],
[ 0, cosTheta, -sinTheta, yTranslation],
[ 0, sinTheta, cosTheta, zTranslation],
[ 0, 0, 0, 1]];

yRot = [
[ cosTheta, 0, sinTheta, xTranslation],
[ 0, 1, 0, yTranslation],
[ -sinTheta, 0, cosTheta, zTranslation],
[ 0, 0, 0, 1]];

zRot = [
[ cosTheta, -sinTheta, 0, xTranslation],
[ sinTheta, cosTheta, 0, yTranslation],
[ 0, 0, 1, zTranslation],
[ 0, 0, 0, 1]];

if axis == "x":
    PrintMat(xRot,transpose)
if axis == "y":
    PrintMat(yRot,transpose)
if axis == "z":
    PrintMat(zRot,transpose)
