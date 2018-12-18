from Day2 import getPuzzleinput
import itertools
import numpy as np

def parseInput(string):
    Numberlist=[]
    for i in string:
        i=i.rpartition('@ ')[2]
        i=i.replace(': ',',').replace('x',',')
        Numberlist.append([int(s) for s in i.split(',') if s.isdigit()])
    return Numberlist

def overlay(proned):
    fabric=np.zeros((1000,1000),dtype=int)
    for id in proned:
        for i,s in itertools.product(range(id[0]-1,id[0]+id[2]-1),range(id[1]-1,id[1]+id[3]-1)):
            fabric[i][s]+=1


    unique,counts=np.unique(fabric,return_counts=True)
    countdict=dict(zip(unique, counts))
    return sum(v for i,v in countdict.items() if i>1), fabric
        #idfabric=[np.array([1][1]) for (x in range(id[0],id[0]+id[2]+1)) for y in range(id[1],id[1]+id[3]+1)]
#        [(fabric[[x,y]]=1) for x in range(id[0],id[0]+id[2]+1) for y in range(id[1],id[1]+id[3]+1)]

def checksingelclaim(fabric,proned):
    for id in proned:
        for i,s in itertools.product(range(id[0]-1,id[0]+id[2]-1),range(id[1]-1,id[1]+id[3]-1)):

            if fabric[i][s]!=1:
                check=0
                break
            else:
                check=1
                continue

        if check==1:
            singelID=id
            break

    return singelID


if __name__=="__main__":

    ids=getPuzzleinput(3)
    proned=parseInput(ids)
    OverlapFields,Fabric=overlay(proned)
    IDsingelclaim=checksingelclaim(Fabric,proned)