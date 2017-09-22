#!/env/bin/python

import random

n=100

def BubbleSort(A):
    m=0
    for i in range(0,n-1):
        for j in range(1,n-i):
            if A[j-1]<A[j]:
                aux=A[j]
                A[j]=A[i]
                A[i]=aux
                m=1
        if m==1: break
        m=0
    return A
    

if __name__=='__main__':
    A=[]
    for i in range(n):
        V=random.randrange(0,n)
        A[i]=V

    print("Los numeros a ordenar son\n")
    print(A)
        
    A=BubbleSort(A)
    print("\n\nLos numeros ordenados son\n")
    print(A)
    
