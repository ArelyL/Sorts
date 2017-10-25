// C++ implementation of Cocktail Sort
#include<bits/stdc++.h>
#include<time.h>
#include<stdlib.h>

#define N 10000

using namespace std;

// Sorts arrar a[0..n-1] using Cocktail sort
void CocktailSort(int a[], int n)
{
    bool swapped = true;
    int start = 0;
    int End= n-1;

    while (swapped)
    {
        // reset the swapped flag on entering
        // the loop, because it might be true from
        // a previous iteration.
        swapped = false;

        // loop from left to right same as
        // the bubble sort
        for (int i = start; i <End; ++i)
        {
            if (a[i] > a[i + 1])
            {
                swap(a[i], a[i+1]);
                swapped = true;
            }
        }

        // if nothing moved, then array is sorted.
        if (!swapped)
            break;

        // otherwise, reset the swapped flag so that it
        // can be used in the next stage
        swapped = false;

        // move the end point back by one, because
        //  item at the end is in its rightful spot
        --End;

        // from right to left, doing the
        // same comparison as in the previous stage
        for (int i =End - 1; i >= start; --i)
        {
            if (a[i] > a[i + 1])
            {
                swap(a[i], a[i+1]);
                swapped = true;
            }
        }

        // increase the starting point, because
        // the last stage would have moved the next
        // smallest number to its rightful spot.
        ++start;
    }
}

/* Prints the array */
void printArray(int a[], int n)
{
    for (int i=0; i<n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

// Driver code
int main()
{
    int arr[N];
    for(int i=0; i<N;i++){
		arr[i]= rand()%N;
		//printf("%i ", A[i]);
	}

    CocktailSort(arr,N);
    printf("Sorted array :\n");
    printArray(arr,N);
    return 0;
}
