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
    start=[[i,ord(i)-64+61] for i in Inp.keys() if not any(i in x for x in Inp.values())]
    start.sort()
    # startval=start[0]
    # queue=start[1:]
#---------------------------working----------------------------------------------
    Q = []
    P = []
    M = []
    Order = Inp.copy()
    t=0

    while Order or Q:

        if t ==0:
            P.extend(start)

        for k in P:
            k[1]-=1
            if k[1]==0:
                M.append(k[0])
                print('Finished ',k[0],t)
                P=[x for x in P if x != k]
                Q.extend(Order[k[0]])
                Q=[t for t in Q if t not in M]
                Q=set(Q)
                Q=sorted(list(Q))
                del Order[k[0]]

        #t += 1

        if len(P)<6 and Q:
            for i in Q:
                if not any(i in x for x in Order.values()):
                    P.append([i,ord(i)+61-64])
                    print('Begin ',i,t)
                    Q=[k for k in Q if k != i]
                    if len(P)>=5:
                        break

        t+=1




    return t









if __name__=="__main__":

    Inp=getPuzzleinput(7)
    pronedInp=proneInput(Inp)
    res=presort(pronedInp)
    duration=work(res)

#-------------------------shorter Internet Solution Part 1------------------------------
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
