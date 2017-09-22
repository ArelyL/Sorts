/* fgets example */
#include <stdio.h>
#include <string.h>

#define N 1000//0

void BubbleSort(char A[N][256]);

int main(){
   FILE * pFile;
   char A[N][256], B[256];
   int i=0;

   pFile = fopen ("Words2.txt" , "r");
   if (pFile == NULL){
        perror ("Error opening file");
        return 0;
   }

    while(fgets (B, 256 , pFile) != NULL ){
        strcpy(A[i], B);
        //puts(A[i]);
        i++;
    }
    fclose (pFile);


	//BubbleSort
   for(int i=0;i<N-1;i++){
		for(int j=1;j<N;j++){
			if(strcmp(A[j-1],A[j])==1){ //como es uno A[j-1]>A[j]
				strcpy(B,A[j]); //A[j] lo copia en B[0]
				strcpy(A[j],A[j-1]);
				strcpy(A[j-1],B);
			}
		}
	}

	for(int i=0; i<N; i++){
		puts(A[i]);
	}

   //BubbleSort(A);

   return 0;
}

void BubbleSort(char A[N][100]){
    char B[256];
    for(int i=0;i<N-1;i++){
		for(int j=1;j<N;j++){
			if(strcmp(A[j-1],A[j])==1){ //como es uno A[j-1]>A[j]
				strcpy(B,A[j]); //A[j] lo copia en B[0]
				strcpy(A[j],A[j-1]);
				strcpy(A[j-1],B);
			}
		}
	}

	for(int i=0; i<N; i++){
		puts(A[i]);
	}
}
