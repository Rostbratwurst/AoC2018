from Day2 import getPuzzleinput
import numpy as np

def borders(coordinates):

    points={coordinates.index(l):(int(i),int(v)) for l in coordinates for i in l.split(', ')[:1] for v in l.split(', ')[1:]}
    maxX=(max(points[key][0] for key in points))
    maxY=(max(points[key][1] for key in points))
    return points,maxX,maxY

def meshgrid(x,y):
    x_ax=np.arange(x)
    y_ax=np.arange(y)
    xx,yy=np.meshgrid(x_ax, y_ax)
    coords=np.dstack([xx,yy]).reshape(-1,2)
    return coords

def distance(p1,p2):

    d=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    return d

def manhatten(grid,points):
    dist=np.zeros((len(grid),2))
    gridndist=np.concatenate((grid,dist),axis=1)
    for p in points:
        #g = np.nditer(grid, flags=['f_index'], op_flags=['readwrite'])
        for i in range(len(gridndist)):
            #print(i[0])
            d=distance(points[p],(gridndist[i][0],gridndist[i][1]))
            if p==0:
                gridndist[i][2] = p
                gridndist[i][3] = d
            elif gridndist[i][3]>d:
                gridndist[i][3]=d
                gridndist[i][2]=p
            elif gridndist[i][3]==d:
                gridndist[i][2] = 99
            else:
                pass
    infinite=[]
    for i in range(len(gridndist)):
        if (gridndist[i][0]==0 or gridndist[i][1]==0) and (gridndist[i][2] not in infinite):
            infinite.append(gridndist[i][2])

    for i in infinite:
        try:
            del points[int(i)]
        except:
            pass
    pointsum=[]

    for p in points:
        pointsum.append(np.count_nonzero(gridndist[:,2]==p))

    # grid=np.zeros((x,y),dtype=int)
    # for i,(v,s) in points.items():
    #     grid[v-1][s-1]=i+1000
    #     if i == 0:
    #         for a in np.nditer(grid, flags=['multi_index'], op_flags=['readwrite']):
    #             a[...] = i
    #     else:
    #         a = np.nditer(grid, flags=['multi_index'], op_flags=['readwrite'])
    #         for k in a:
    #             print(a[0], a.multi_index)
    #             #print(type(a.multi_index))
    #             try:
    #                 a.__next__()
    #             except:
    #                 break


        # elif
        # a = np.nditer(grid, flags=['multi_index'], op_flags=['readwrite'])
        #     for i in range(1000000):
        #         print(a[0],a.multi_index)
        #         a.__next__()
        #     if i == 0:
        #         a[...]=0
        #     elif abs(l-points[i+1][0])+abs(v-points[i+1][1]):
        #         a[...]=


    return gridndist,infinite,pointsum

if __name__=="__main__":

    coordinates=getPuzzleinput(6)
    points,x,y=borders(coordinates)
    grid=meshgrid(x,y)
    gd,inf,res=manhatten(grid,points)