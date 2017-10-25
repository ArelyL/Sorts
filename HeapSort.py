#!/env/bin/python

import random
import math

n=100

def Heap(N, Large):
    M=[[-10 for i in range(3)] for i in range(int(Large/2)-1)]
    j=int(Large/2)-2

    #calcular padres he hijos
    for i in range(int(Large/2)-1):
        M[j][0]=i
        M[j][1]=2*i+1
        M[j][2]=2*i+2
        j-=1

    #print M

    if Large%2==0:
        #print Large/2 -1, Large-1
        R=Swaping(N[Large/2-1], N[Large-1], -100)
        N[Large/2 -1]=R[0]
        N[Large -1]=R[1]

    for i in range(int(Large/2)-1):
        R=Swaping(N[M[i][0]], N[M[i][1]], N[M[i][2]])
        N[M[i][0]]=R[0]
        N[M[i][1]]=R[1]
        N[M[i][2]]=R[2]
        #print N[M[i][0]], N[M[i][1]], N[M[i][2]]

    N[0], N[Large-1] = N[Large-1], N[0]
    Large-=1

    if Large>0:
        Heap(N, Large)
    else:
        R=Swaping(N[0], N[1], N[2])
        N[2]=R[0]
        N[1]=R[1]
        N[0]=R[2]
        N=N[::-1]
        print N#, Large
    

def Swaping(N1, N2, N3):
    if N1>N2:
        N1, N2 = N2, N1
        
    if N3!=-100:
        if N1>N3:
            N1, N3 = N3, N1

    N=[N1, N2, N3]

    return N


if __name__=='__main__':
    N=[0 for i in range(n)]

    for i in range(n):
        N[i]=random.randint(0,n)

   
    print "Los numeros a ordenar son\n", N
    print "Los numeros ordenados son\n"
    Heap(N, n)
    

        
