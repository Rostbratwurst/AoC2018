from Day2 import getPuzzleinput

def borders(coordinates):
    x=[]
    y=[]
    for l in coordinates:
        i,v = l.split(', ')
        x.append(int(i))
        y.append(int(v))
    return max(x),max(y)




if __name__=="__main__":

    coordinates=getPuzzleinput(6)
    X,Y=borders(coordinates)