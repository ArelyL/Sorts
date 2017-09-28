#!/env/bin/python

import random

n=10

def InsertSort(A, B):
 
    if B<=A[0]: A=[B]+A
    elif A[n-1]<=B: A=A+[B]
    else:
        for i in range(0, n-1):
            if A[i]<=B and B<=A[i+1]:
                A.insert(i+1,B)
                break
    return A

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
        
    M=BubbleSort(A)
    print("\n\nLos numeros ordenados son\n")
    print(M)

    R=InsertSort(M,6)
    print("\n\nSe inserto el numero 5 en la cadena\n")
    print(R)
    
    R=InsertSort(R,256)
    print("\n\nSe inserto el numero 256 en la cadena\n")
    print(R)

    R=InsertSort(R,-3)
    print("\n\nSe inserto el numero -3 en la cadena\n")
    print(R)
