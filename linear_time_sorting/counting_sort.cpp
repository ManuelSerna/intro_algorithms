//***********************************************
// Counting Sort algorithm
// Run time: Theta(n + k)
//***********************************************
#include <iostream>
using namespace std;

const int SIZE = 8;// length n of input/output array

//===============================================
// Array printing helper function for array P.
//===============================================
void print(int P[], int length)
{
    for(int i = 0; i < length; i++)
    {
        cout << P[i] << " ";
    }
    cout << endl;
}

//===============================================
/*
    Counting sort
    Inputs:
            A --original array with unsorted values.
            b --output array that will be sorted.
            k --the max value of any element in A.
*/
//===============================================
void counting_sort(int A[], int B[], int k)
{
    /* PART (a) */
    
    // Let C be a new array--the counting array (k times)
    int C[k+1];
    
    for(int i = 0; i <= k; i++)
    {
        C[i] = 0;
    }
    
    /*
        If value of input element is i, increment C[i]
        Go through A (length n), if A[i] appears, then increment the 
        count in C where the index is an element that may or may not 
        appear in A, and the element at index i is the count (n times).
    */
    for(int j = 0; j < SIZE; j++)
    {
        C[A[j]] = C[A[j]] + 1;
    }
    
    // C[i] now contains the number of elements equal to i.
    // Now visualize after initializing and counting.
    print(C, k+1);
    
    /* PART (b) */
    
    for(int i = 1; i <= k; i++)
    {
        C[i] = C[i] + C[i-1];
    }
    
    // C[i] now contains the number of elements less than or equal to i
    // Now visualize cumulative summation.
    print(C, k+1);
    
    /* PART (c) */
    
    for(int j = SIZE-1; j > -1; j--)
    {
        B[C[A[j]]-1] = A[j];
        cout << B[C[A[j]]] << endl;
        
        C[A[j]] = C[A[j]] - 1;
        cout << C[A[j]] << endl;
        
        print(C, k+1);
        print(B, SIZE);
    }
}

//===============================================
// MAIN
//===============================================
int main()
{
    // A: input array with unsorted values
    int A[SIZE] = {2, 5, 3, 0, 2, 3, 0, 3};
    
    // B: output array with sorted values
    int B[SIZE] = {-1, -1, -1, -1, -1, -1, -1, -1};
    int k = 5;// max value of any element in A
    
    // Call counting sort procedure
    counting_sort(A, B, k);
    
    cout << "==============================" << endl;
    cout << "Sorted array: ";
    print(B, SIZE);
    
    return 0;
}
