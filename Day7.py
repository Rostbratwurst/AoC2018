from Day2 import getPuzzleinput
import numpy as np

def proneInput(Inp):
    return [(x.split(' ')[1], x.split(' ')[-3])for x in Inp]


def order(Inp):
    letter=['abcdefghijklmnopqrstuvwxyz']
    manual=[]


    it=0
    while Inp:

        if it==0:
            manual.append(Inp[0][0])
            stage = Inp[0][1]
            del Inp[0]

        nexts = []
        dellist=[]
        for ind, befaft in enumerate(Inp):
            if befaft[0] == stage or  befaft[0] in stage:
                nexts.append(befaft[1])
                dellist.append(ind)
        manual.extend(sorted(nexts))
        stage=nexts
        for n in sorted(dellist,reverse=True):
            del(Inp[n])

        it += 1



    return manual




if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=order(pronedInp)