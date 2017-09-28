#!/env/bin/python

import random

n=100

def InsertSort(A):

    M=[A[0]]
    k=2

    for i in range(1,n):
        if A[i]<M[0]:
            M=[A[i]]+M
        elif A[i]>=M[len(M)-1]:
            M=M+[A[i]]
        else:
            for j in range(1,len(M)):
                if A[i]>=M[j-1] and A[i]<M[j]:
                    M.insert(j,A[i])
                    break
                k+=1
            
    #print(M)


if __name__=='__main__':
    A=[0 for i in range(n)]

    for i in range(n):
        A[i]=random.randint(0,n)

    #print("Los numeros a ordenar son\n", A)

    #print("\nLos numeros ordenados son\n")
    InsertSort(A)

        
