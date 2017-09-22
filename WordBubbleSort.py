#!/env/bin/python

import random

n=10000
    
def BubbleSortWords(Lista):
    k=0
    m=0
    n=len(Lista)
    
    for i in range(0,n-1):
        for j in range(1,n):
            if Lista[j]<Lista[j-1]:
                Lista[j],Lista[j-1]=Lista[j-1],Lista[j]
            k+=1
    print(k)

    #print(m)
    print(Lista)

if __name__=='__main__':
     Lista=[]

     archivo=open("Words.txt","r")
     Lista=archivo.readlines()

     BubbleSortWords(Lista)

