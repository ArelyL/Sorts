#include<stdio.h>
#include<time.h>
#include<stdlib.h>

#define N 10


int main(){
	int A[N];
    int i;
	printf("Lista de numeros a ordenar\n\n");

	for(i=0;i<N;i++){
		A[i]= rand()%N;
		//printf("%i ", A[i]);
	}

	printf("\n\n");
	//system("pause");
	return 0;

}
