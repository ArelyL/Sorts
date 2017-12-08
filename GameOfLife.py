#!/env/bin/python
import random

M=11 #Numero de renglones
N=16 #muero de columnas

def Matrix():
     #L= [[0]* 10 for i in range(10)]

     ##Genera la matriz con la celulas vivas (1) y las celulas muertas (0) en forma aleatoria
     #for i in range(M):
     #    for j in range(N):
     #        if 18<random.randint(0,99)<60:
     #            L[i][j]=1

     #Matriz inicial pentadecatlón!
       # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
     L=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #5
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0], #6
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #11

     for i in range(M):
         print(L[i])

     return L

def GameOfLife(A):
     B= [[0]* N for i in range(M)]
     for i in range(M):
          for j in range(N):
               B[i][j]=A[i][j]
     #esquina [0,0]
          a=A[0][1]+A[1][1]+A[1][0]
          if A[0][0]==1 and a==1: B[0][0]=0
          if A[0][0]==0 and a==3: B[0][0]=1
     #esquina[0,N]
          a=A[0][N-2]+A[1][N-2]+A[1][N-1]
          if A[0][N-1]==1 and a==1: B[0][N-1]=0
          if A[0][N-1]==0 and a==3: B[0][N-1]=1
     #esquina [M,0]
          a=A[M-2][0]+A[M-2][1]+A[M-1][1]
          if A[M-1][0]==1 and a==1: B[M-1][0]=0
          if A[M-1][0]==0 and a==3: B[M-1][0]=1
     #esquina [M,N]
          a=A[M-2][N-1]+A[M-2][N-2]+A[M-1][N-2]
          if A[M-1][N-1]==1 and a==1: B[M-1][N-1]=0
          if A[M-1][N-1]==0 and a==3: B[M-1][N-1]=1
 
     #renglon 1 y M
     Num=[0, 1, 4, 5]  
     for i in range(1, N-1):
          #renglon 0
               #print("Celula[0,",i,"]: ", A[0][i])
               #print("Vecinos: ", A[0][i-1]," ", A[0][i+1], " ", A[1][i-1], " ", A[1][i], " ", A[1][i+1])
               a=A[0][i-1]+A[0][i+1]+A[1][i-1]+A[1][i]+A[1][i+1]
               #print("Suma de los veccinos: ", a)
               if A[0][i]==1 and a in Num: B[0][i]=0
               if A[0][i]==0 and a==3: B[0][i]=1
          #Renglon M
               b=A[M-1][i-1]+A[M-1][i+1]+A[M-2][i-1]+A[M-2][i]+A[M-2][i+1]
               if A[M-1][i]==1 and b in Num: B[M-1][i]=0
               if A[M-1][i]==0 and b==3: B[M-1][i]=1

     #columna 0 y N
     for i in range(1, M-2):
          #columna 0
               a=A[i-1][0]+A[i+1][0]+A[i-1][1]+A[i][1]+A[i+1][1]
               if A[i][0]==1 and a in Num: B[i][0]=0
               if A[i][0]==0 and a==3: B[i][0]=1
          #columna N
               b=A[i-1][N-1]+A[i+1][N-1]+A[i-1][N-2]+A[i][N-2]+A[i+1][N-2]
               if A[i][N-1]==1 and b in Num: B[i][N-1]=0
               if A[i][N-1]==0 and b==3: B[i][N-1]=1
          
     #Centro
     Num2=[0, 1, 4, 5, 6, 7, 8]
     for i in range(1, M-1):
          for j in range(1,N-1):
               a=A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]+A[i][j-1]+A[i][j+1]+A[i+1][j-1]+A[i+1][j]+A[i+1][j+1]
               #print("Numero de vecinos vimos para [", i,",",j,"]: ",a)
               if A[i][j]==1 and a in Num2: B[i][j]=0
               if A[i][j]==0 and a==3: B[i][j]=1
     

     for i in range(M):
          print(B[i])
         
    #primer renglon
    #for i in range(1N):
     return B



if __name__=='__main__':

     print("iteracion 0")
     A=Matrix()
     for i in range(0,20):
          print("Iteracion ",i+1)
          B=GameOfLife(A)
          A=B



#Si la célula es viva : Si tiene 2 o 3 vecinos vivos entonces vive, de otra manera muere                        
#Si la celula es muerta: solamente revive si tiene exactamente 3 vecinos vivos
