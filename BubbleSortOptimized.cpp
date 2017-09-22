#include<stdio.h>
#include<time.h>
#include<stdlib.h>

#define N 10000

void Buble(int A[N]);

int main(){
	int A[N];

	//printf("Lista de numeros a ordenar\n\n");

	for(int i=0; i<N;i++){
		A[i]= rand()%N;
		//printf("%i ", A[i]);
	}

	Buble(A);
	printf("\n\n");
	//system("pause");
	return 0;

}

void Buble(int A[N]){
	int aux;
	int m=0;

   for(int i=0;i<N-1;i++){
		for(int j=1;j<N-i;j++){
			if(A[j-1]>A[j]){
				aux=A[j];
				A[j]=A[j-1];
				A[j-1]=aux;
				m=1;
			}
		}
		if(m==0) break;
		m=0;
	}

   printf("\n\nLos numeros ordenados son: \n\n");

	for(int i=0; i<N; i++){
		printf("%i ", A[i]);
	}

}
