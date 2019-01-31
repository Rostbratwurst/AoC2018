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
    start=[(i,ord(i)-64) for i in Inp.keys() if not any(i in x for x in Inp.values())]
    start.sort()
    # startval=start[0]
    # queue=start[1:]
#---------------------------working----------------------------------------------
    InpCop = dict(Inp)
    InProgress=set(start)
    t=0
    queue=[]
    while InpCop or queue:
        for elem in InProgress:
            if elem[1]==0:
                manual.append(elem[0])
                queue.extend(InpCop[elem[0]])
                InpCop.pop(elem[0])
        queue = sorted(set(queue))
        queue = [x for x in queue if x not in (manual and InProgress)]
        InProgress=set(x for x in InProgress if x[1]>0)
        InProgress=set((x,y-1) for x,y in InProgress)
        #InProgress=set([x for x in InProgress if x not in manual])
        # try:
        #     queue.extend(InpCop[startval])
        #     del InpCop[startval]
        # except KeyError:
        #     pass
        # queue=sorted(set(queue))
        # queue=[x for x in queue if x not in manual]
        Tasks=[(x,ord(x)+61-64)for x in queue if not any(x in i for i in InpCop.values())]
        queue=[x for x in queue if not any(x in i for i in Tasks)]

        n=0
        while len(InProgress)<5 and Tasks:
            try:
                InProgress.update([Tasks[n]])
            except IndexError:
                break
            n+=1




        # try:
        #     startval=sorted(Task)[0]
        # except IndexError:
        #     pass
        t+=1

    return ''.join(manual),t









if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=presort(pronedInp)
    man,duration=work(res)

#-------------------------shorter Internet Solution------------------------------
# from collections import defaultdict, deque
# from Day2 import getPuzzleinput
#  # Edges
# E = defaultdict(list)
#  # In-degree
# D = defaultdict(int)
# Inp=getPuzzleinput(7)
# for line in Inp:
#     words = line.split()
#     x = words[1]
#     y = words[7]
#     E[x].append(y)
#     D[y] += 1
#
# Q=[]
# for k in E:
#     if D[k] == 0:
#         Q.append(k)
#
#
# ans = ""
# while Q:
#     x = sorted(Q)[0]
#     Q = [y for y in Q if y!=x]
#     ans += x
#     for y in E[x]:
#         D[y] -= 1
#         if D[y] == 0:
#             Q.append(y)
# print (ans)