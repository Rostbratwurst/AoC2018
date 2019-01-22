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
            index_aft=[i for i, x in enumerate(manual) if aft in x]
            index_bef=[i for i, x in enumerate(manual) if bef in x]
            if len(index_bef)>1 or len(index_aft)>1:
                print('------------------FEHLER-----------------------')
                break

            if not manual:                                                  #would fail if empty lists in list
                app([bef])
                app([aft])

            elif index_aft and not index_bef:
                try:
                    manual[index_aft[0]-1].append(bef)
                except IndexError:
                    manual.insert(index_aft[0],[bef])
                except:
                    print("Something else went wrong")

            elif index_bef and not index_aft:
                try:
                    manual[index_bef[0]+1].append(aft)
                except IndexError:
                    manual.insert(index_bef[0]+1,[aft])
                except:
                    print("Something else went wrong")
            Inp.remove((bef,aft))

    manual=[sorted(s) for i,s in enumerate(manual)]
    return manual




if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=order(pronedInp)