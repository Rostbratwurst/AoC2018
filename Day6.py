from Day2 import getPuzzleinput
import numpy as np

def borders(coordinates):

    points={coordinates.index(l):(int(i),int(v)) for l in coordinates for i in l.split(', ')[:1] for v in l.split(', ')[1:]}
    maxX=(max(points[key][0] for key in points))
    maxY=(max(points[key][1] for key in points))
    return points,maxX,maxY

def manhatten(x,y,points):
    grid=np.zeros((x,y),dtype=int)
    for i,(v,s) in points.items():
        grid[v-1][s-1]=i+1000
        if i == 0:
            for a in np.nditer(grid, flags=['multi_index'], op_flags=['readwrite']):
                a[...] = i
        else:
            a = np.nditer(grid, flags=['multi_index'], op_flags=['readwrite'])
            for k in a:
                print(a[0], a.multi_index)
                print(type(a.multi_index))
                try:
                    a.__next__()
                except:
                    break


        # elif
        # a = np.nditer(grid, flags=['multi_index'], op_flags=['readwrite'])
        #     for i in range(1000000):
        #         print(a[0],a.multi_index)
        #         a.__next__()
        #     if i == 0:
        #         a[...]=0
        #     elif abs(l-points[i+1][0])+abs(v-points[i+1][1]):
        #         a[...]=


    return grid

if __name__=="__main__":

    coordinates=getPuzzleinput(6)
    points,x,y=borders(coordinates)
    catch=manhatten(x,y,points)