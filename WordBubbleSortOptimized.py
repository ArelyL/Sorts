#!/env/bin/python

import random

n=10000
    
def BubbleSortWords(Lista):
    k=0
    m=0
    n=len(Lista)
    
    for i in range(0,n-1):
        for j in range(1,n-i):
            if Lista[j]<Lista[j-1]:
                Lista[j],Lista[j-1]=Lista[j-1],Lista[j]
                m=1
            k+=1
        if m==0: break
        m=0;

    print(k)
    print(Lista)


if __name__=='__main__':
     Lista=[]

     archivo=open("Words.txt","r")
     Lista=archivo.readlines()

     BubbleSortWords(Lista)
