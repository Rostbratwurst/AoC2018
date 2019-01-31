from collections import Counter
import numpy as np
import itertools as it
import difflib
theString = 'zihrtxgmwcfpbunoleydukjmqv'
theString2 = ['zihrtxgmwcfpbunoleydukjmqk']
stinglist =['zihrtxgmwcfpbunoleydukjmqv','zihrtxgmwcfpbunoleydukjmqk']
# newList = Counter(theString)
# print(newList)
# counter_counter=Counter(newList.values())
# print(counter_counter)
# if counter_counter[2]==2:
#     print(counter_counter.items())

# meintupel=(1,2,3,4,5,6)
# meinmix=[meintupel,11,22]
# for i,v in meinmix.iteritems():
#     print(i,v)

# d=difflib.Differ()
# diff=d.compare(theString1,theString2)
# u=difflib.get_close_matches('qv',stinglist,1,0)

# print(stinglist)
# print(u)
# print('\n'.join(diff))


# print (theString.rpartition('buno')[2])

#[int(s) for s in str.split() if s.isdigit()]#
#
# test1=[1,2,3,5,6,7,8,9]
# test2=[7,8,9]
# for i in test1 for k in test2:
#     print (i,j)


# X = np.zeros((100, 200, 300))
# print(X.shape[0])
#
#
# for i,s in it.product(range(30, 52), range(1, 18)):
#     print(i,s)

# def notlast(itr):
#     itr = iter(itr)  # ensure we have an iterator
#     prev = itr.__next__()
#     for item in itr:
#         yield prev
#         prev = item
#
# meiniterator=notlast(test1)
#
# for i in meiniterator:
#     print(i)
from collections import defaultdict, deque

# Edges
E = defaultdict(list)
# In-degree
D = defaultdict(int)
for line in open('input_day7.txt'):
    words = line.split()
    x = words[1]
    y = words[7]
    E[x].append(y)
    D[y] += 1

for k in E:
    E[k] = sorted(E[k])

# time
t = 0
# Events
EV = []
# Work queue
Q = []


def add_task(x):
    Q.append(x)


def start_work():
    global Q
    while len(EV) < 5 and Q:
        x = min(Q)
        Q = [y for y in Q if y != x]
        print('Starting {} at {}'.format(x, t))
        EV.append((t + 61 + ord(x) - ord('A'), x))


for k in E:
    if D[k] == 0:
        add_task(k)
start_work()

while EV or Q:
    t, x = min(EV)
    print(t, x)
    EV = [y for y in EV if y != (t, x)]
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            add_task(y)
    start_work()

print(t)

# ans = ""
# while Q:
#    x = sorted(Q)[0]
#    Q = [y for y in Q if y!=x]
#    ans += x
#    for y in E[x]:
#        D[y] -= 1
#        if D[y] == 0:
#            Q.append(y)
# print ans
#