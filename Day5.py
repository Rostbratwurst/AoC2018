from Day2 import getPuzzleinput
from Day4 import customiter
import re

def reaction(polymer):
    # polymercopy=polymer
    reactive=True
    while reactive:

        index=0
        startlen=len(polymer)
        while index < len(polymer)-1:
            if polymer[index].lower()==polymer[index+1].lower() and polymer[index] != polymer[index+1]:
                del polymer[index + 1]
                del polymer[index]

            else:
                pass
            index+=1
        endlen=len(polymer)
        if startlen==endlen:
            reactive=False

    return polymer

def badunit(reducedpolymer):
    char='abcdefghijklmnopqrstuvwxyz'
    polymerlength={}
    for c in char:
        reduced=[i for i in reducedpolymer if i.casefold() != c]
        #reduced=re.sub('c','',reducedpolymer)
        shortpoly=reaction(reduced)
        polymerlength[c]=len(shortpoly)
    return polymerlength
if __name__=="__main__":

    string=getPuzzleinput(5)
    string=[i for i in string[0]]
    #string=['a','a','b','c','C','c','d','D','B','A','x']
    # polymerraw=getPuzzleinput(5)[0]
    # polymer=[i for i in polymerraw]
    # # twoiters=customiter(polymer)
    reaction(string)
    bestdelete=badunit(string)