#!/env/bin/python

import random
    
def BubbleSortWords(Lista):
    k=0
    m=0
    n=len(Lista)
    q=0
    
    for i in range(0,n):
        for j in range(i, n-i-1):
            if Lista[j+1]<Lista[j]:
                Lista[j+1],Lista[j]=Lista[j],Lista[j+1]
                m=1
            k+=1
        for r in range(n-2-i,i):
            if Lista[r]<Lista[r-1]:
                Lista[r],Lista[r-1]=Lista[r-1],Lista[r]
                m=1
            k+=1
        if m==0: break
        m=0;

    print(k)
    print(Lista)


if __name__=='__main__':
     Lista=[]

     archivo=open("Palabras.txt","r")
     Lista=archivo.readlines()

     BubbleSortWords(Lista)
