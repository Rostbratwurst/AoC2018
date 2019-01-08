from Day2 import getPuzzleinput
import numpy as np

def borders(coordinates):
    x=[]
    y=[]
    coordinates={l:(int(i),int(v)) for l in}
    for l in coordinates:
        i,v = l.split(', ')
        x.append(int(i))
        y.append(int(v))
        coordinates[l]={L:(int(i),int(v))}
    return max(x),max(y)

def manhatten(x,y,*points):
    grid=np.zeros((x,y),dtype=int)


if __name__=="__main__":

    coordinates=getPuzzleinput(6)
    X,Y=borders(coordinates)