from Day2 import getPuzzleinput
import numpy as np

def borders(coordinates):

    points={coordinates.index(l):(int(i),int(v)) for l in coordinates for i in l.split(', ')[:1] for v in l.split(', ')[1:]}
    maxX=(max(points[key][0] for key in points))
    maxY=(max(points[key][1] for key in points))
    return points,maxX,maxY

def manhatten(x,y,*points):
    grid=np.zeros((x,y),dtype=int)


if __name__=="__main__":

    coordinates=getPuzzleinput(6)
    points,x,y=borders(coordinates)