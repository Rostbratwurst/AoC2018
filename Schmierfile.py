from collections import Counter
import difflib
theString = 'zihrtxgmwcfpbunoleydukjmqv'
theString2 = ['zihrtxgmwcfpbunoleydukjmqk']
stinglist =['zihrtxgmwcfpbunoleydukjmqv','zihrtxgmwcfpbunoleydukjmqk']
newList = Counter(theString)
print(newList)
counter_counter=Counter(newList.values())
print(counter_counter)
if counter_counter[2]==2:
    print(counter_counter.items())

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

test1=[1,2,3]
test2=[7,8,9]
for i,j in itertools(test1,test2)):
    print (i,j)