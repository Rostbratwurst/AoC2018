from Day2 import getPuzzleinput
import datetime

import itertools
import numpy as np

def sortbytime(input):
    return input.sort(key=lambda x: datetime.datetime.strptime(x.rpartition(']')[0].replace('[',''), "%Y-%m-%d %H:%M"))

def customiter(input):
    n=0
    while True:
        try:
            yield input[n],input[n+1]

        except IndexError:
            return
        n+=1

def sumsleeptime(input):
    Guards={}
    for stamp,stampon in customiter(ids):
        #activeGuard=None
        if 'Guard' in stamp:
            activeGuard =int(''.join([i for i in stamp.rpartition('#')[2] if i.isdigit()]))
            if activeGuard not in Guards:
                Guards.update({activeGuard:0})
        elif 'falls' in stamp:
            Guards[activeGuard]+=(int(stampon[15:17])-int(stamp[15:17]))
        else:
            pass
    return Guards,max(Guards, key=lambda k: Guards[k])

def mostminute(sleepmaster):

    minutes=np.zeros(60)
    active=0
    for stamp, stampon in customiter(ids):
        if str(sleepmaster) in stamp:
            active=1
        elif 'falls' in stamp and active==1:
           for i in range(int(stamp[15:17]),int(stampon[15:17])):
               minutes[i]+=1
        elif 'wakes' in stamp and active==1:
            continue
        else:
            active=0
            continue
    return minutes

if __name__=="__main__":

    ids=getPuzzleinput(4)
    sortbytime(ids)
    Numbergurads,sleepmaster=sumsleeptime(ids)
    sleepsum=mostminute(sleepmaster)
    result=sleepmaster*np.argmax(sleepsum)
    Guradminutes = [{i:(np.where(mostminute(i)==np.max(mostminute(i))),np.max(mostminute(i)))} for i,k in Numbergurads.items()]
    # for i,k in Numbergurads.items():
    #     mostminute(i)
    #     Guard



