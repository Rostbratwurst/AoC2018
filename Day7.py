from Day2 import getPuzzleinput
import numpy as np

def proneInput(Inp):
    return [(x.split(' ')[1], x.split(' ')[-3])for x in Inp]


def order(Inp):
    manual=[]
    app=manual.append
    ins=manual.insert
    index=manual.index
    while Inp:
        for bef, aft in Inp:

            if all(bef not in s for s in manual) and all(aft not in s for s in manual):
                app(bef)
                app(aft)

            elif any(aft in s for s in manual) and all(bef not in s for s in manual):
                ins(index(aft),bef)

            elif all(aft not in s for s in manual) and any(bef in s for s in manual):
                ins(index(bef),aft)

            Inp.remove((bef,aft))

    return manual




if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=order(pronedInp)