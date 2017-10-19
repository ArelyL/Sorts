#!/env/bin/python

import random
import math

T=100

def MergeSort(N):
    m=len(N[0])
    j=0
    M=[[0 for i in range(m*2)] for i in range(int(len(N)/2.0))]

    for i in range(0,len(N)-1,2):
        M[j]=Sort(N[i],N[i+1])
        j+=1

    if len(N)%2!=0:
        M+=[N[len(N)-1]]

    if len(M[0])<T:
        MergeSort(M)
    else:
        print(M,"\n")


def Sort(N, M):
    n=len(N)
    m=len(M)
    R=[0 for i in range(n+m)]
    #K=[0 for i in range(n+m)]
    Max=max(max(N), max(M))

    for i in range(n+m):
        R[i]=min(min(N), min(M))
        if min(min(N), min(M))==min(N):
            Replace(Max, N)
        else:
            Replace(Max, M)
    
    return R

def Replace(num, N):
    Min=min(N)
    for i in range(len(N)):
        if N[i]==Min:
            N[i]=num+1
            break
        
    return N

def Equal(N):
    R=[0 for i in range(len(N))]

    for i in range(len(N)-1):
        R[i]=N[i]

    return R

if __name__=='__main__':
    N=[[0] for i in range(T)]
    
    for i in range(T):
        N[i][0]=random.randint(0,T)  
    
    print("Los numeros a ordenar son: \n", N)
    
    print("\nLos numeros ordenados son: \n")
    MergeSort(N)


    

        
