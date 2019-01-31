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
#---------------------------working----------------------------------------------
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
        Task=[x for x in queue if not any(x in i for i in InpCop.values()) ]
        try:
            startval=sorted(Task)[0]
        except IndexError:
            pass

    return ''.join(manual)



if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=presort(pronedInp)
    man=work(res)

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