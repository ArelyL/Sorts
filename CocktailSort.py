import random
import math

n=100


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
 
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1

if __name__=='__main__':
    N=[0 for i in range(n)]

    for i in range(n):
        N[i]=random.randint(0,n)
        
print "\nArray is:\n", N
cocktailSort(N)

print "\nSorted array is:\n", N






