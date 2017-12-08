/* fgets example */
#include <stdio.h>

#define N 10

void BubbleSort(char A[][256]);

int main(){
   FILE * pFile;
   char mystring[N][256];
   int i;

   pFile = fopen ("Palabras.txt" , "r");
   if (pFile == NULL) perror ("Error opening file");
   else {
		i=0;
		while(fgets (mystring[i], 100 , pFile) != NULL ){
	       //puts (mystring[i]);
	       i++;
		}
   }
   BubleSort(mystring);
     
   fclose (pFile);
   return 0;
}


void BubbleSort(char A[][256]){
	char c;
	int i,j,k,s;
	for(i=0;i<N;i++){
		for(j=0;j<strlen(A[i])-1;j++){
			for(k=0;k<strlen(A[i])-1;k++){
				if(A[i][k]>A[i][k+1]){		
					c=A[i][k];
					A[i][k]=A[i][k+1];
					A[i][k+1]=c;
				}
			}
		}
	printf("%s",A[i]);
	}
}*/

