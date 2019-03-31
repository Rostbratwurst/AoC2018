from Day2 import getPuzzleinput
import numpy as np

st=0
def newstage(nodes):
    global st
    st+=1



def metasum(Inp):
    metasumme=0
    depth=0
    #1: Tree depth level
    #2: child nodes
    #3: Meta entrys
    tree=np.empty([1,3])
    i=0
    while i<len(Inp):
        if Inp[i]==0:
            i+=1
            metaentry=Inp[i]
            i+=1
            while metaentry:
                metasumme+=Inp[i]
                metaentry-=1
            if depth>0:
                depth-=1
        elif Inp[i]!=0:
            try:
                if i==0:
                    tree = np.array([[depth,Inp[i],Inp[i+1]]])
                else:
                    np.append(tree,[[depth,Inp[i],Inp[i+1]]],axis=0)
            except:
                print('End reached')
            i+=1
    return metasumme












if __name__=="__main__":
    Inp=getPuzzleinput(8)
    Inp=[int(i) for i in Inp[0].split()]
    result=metasum(Inp)


