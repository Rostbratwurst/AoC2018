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
    fabric=np.zeros((1000,1000))
    for id in proned:
        for x,y in zip()


    return fabric

if __name__=="__main__":

    ids=getPuzzleinput(3)
    proned=parseInput(ids)
    whaaat=overlay(proned)
