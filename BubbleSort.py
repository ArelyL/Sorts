#!/env/bin/python

import random

n=10000

def BubbleSort(A):
    for i in range(1,n):
        for j in range(0,n-1):
            if A[i]<A[j]:
                aux=A[j]
                A[j]=A[i]
                A[i]=aux
    
    

if __name__=='__main__':
    A=[[]]
    for i in range(n):
        V=random.randint(0,99)
        A.append(V)

    #print("Los numeros a ordenar son\n")
    #print(A)
        
    BubbleSort(A)
    print("\n\nLos numeros ordenados son\n")
    print(A)
    
