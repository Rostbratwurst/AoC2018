from Day2 import getPuzzleinput
import numpy as np
import itertools
import collections

def proneInput(Inp):
    return [(x.split(' ')[1], x.split(' ')[-3])for x in Inp]
#
#
def presort(Inp):
    d=collections.defaultdict(list)
    for k,v in Inp:
        d[k].append(v)
        d[k].sort()

    return d

def work(Inp):
    manual=[]
#------------------------start poin and queue------------------------------------
    start=[i for i in Inp.keys() if not any(i in x for x in Inp.values())]
    start.sort()
    startval=start[0]
    queue=start[1:]
#---------------------------working---------------------------------------------
    InpCop = dict(Inp)

    while InpCop or queue:
        manual.append(startval)
        try:
            queue.extend(InpCop[startval])
            del InpCop[startval]
        except KeyError:
            pass
        queue=sorted(set(queue))
        queue=[x for x in queue if x not in manual]
        try:
            startval=queue[0]
            queue=queue[1:]
        except IndexError:
            pass

    return ''.join(manual)











if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=presort(pronedInp)
    man=work(res)

