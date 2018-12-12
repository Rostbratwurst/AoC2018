from Day2 import getPuzzleinput
import itertools

def parseInput(string):
    Numberlist=[]
    for i in string:
        i=i.rpartition('@ ')[2]
        i=i.replace(': ',',').replace('x',',')
        Numberlist.append([int(s) for s in i.split(',') if s.isdigit()])
    return Numberlist

def overlay(proned):
    for pro1, pro2 in itertools.combinations(proned, 2):
        max(pro1[0],pro2[0])-min(pro1[0],pro2[0])


if __name__=="__main__":

    ids=getPuzzleinput(3)
    proned=parseInput(ids)
    overlay(proned)
