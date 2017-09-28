#!/env/bin/python

import random

n=100

def BubbleSort(A):
    m=0
    for i in range(0,n-1):
        for j in range(1,n-i):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
                m=1
        if m==0: break
        m=0
    return A
    

if __name__=='__main__':
    A=[0 for i in range(n)]

    for i in range(n):
        A[i]=random.randint(0,n-1)

    print("Los numeros a ordenar son\n")
    print(A)
        
    A=BubbleSort(A)
    print("\n\nLos numeros ordenados son\n")
    print(A)
    
