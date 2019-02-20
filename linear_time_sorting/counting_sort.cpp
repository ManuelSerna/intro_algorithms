//**********************************************/
// Counting Sort algorithm
//**********************************************/
#include <iostream>
using namespace std;

const int SIZE = 8;// length n of input/output array

//===============================================
// Counting sort
//===============================================
void counting_sort(int A[], int B[], int k)
{
    //-------------------------------------------
    // PART (a)
    //-------------------------------------------
    // Let C be a new array--the counting array (k times)
    int C[k+1];
    for(int i = 0; i <= k; i++)
    {
        C[i] = 0;
    }
    
    // If value of input element is i, increment C[i]
    // Go through A (length n), if A[i] appears, then increment the count in C where the index is an element that may or may not appear in A, and the element at index i is the count (n times).
    for(int j = 0; j < SIZE; j++)
    {
        //int temp = A[j];
        C[A[j]] = C[A[j]] + 1;
    }
    // C[i] now contains the number of elements equal to i
    
    // Visualize C after above loop
    cout << "Array C (a): ";
    for(int i = 0; i <= k; i++)
    {
        cout << C[i] << " ";
    }
    cout << endl;
    
    //-------------------------------------------
    // PART (b)
    //-------------------------------------------
    for(int i = 1; i <= k; i++)
    {
        C[i] = C[i] + C[i-1];
    }
    // C[i] now contains the number of elements less than or equal to i
    
    // Visualize C after above loop
    cout << "Array C (b): ";
    for(int i = 0; i <= k; i++)
    {
        cout << C[i] << " ";
    }
    cout << endl;
    
    //-------------------------------------------
    // PART (c)
    //-------------------------------------------
    // Note: A and B start at index 1, adjust program for that
    for(int j = SIZE-1; j > -1; j--)
    {
        B[C[A[j]]-1] = A[j];
        cout << B[C[A[j]]] << endl;
        
        C[A[j]] = C[A[j]] - 1;
        cout << C[A[j]] << endl;
        
        cout << "C: ";
        for(int i = 0; i <= k; i++)
        {
            cout << C[i] << " ";
        }
        cout << endl;

        cout << "B: ";
        for(int i = 0; i < SIZE; i++)
        {
            cout << B[i] << " ";
        }
        cout << "\n----------------------" << endl;//
    }
    
    
    //-------------------------------------------
    // Output sorted array B
    //-------------------------------------------
    cout << "==============================\n";
    cout << "Sorted array: ";
    for(int i = 0; i < SIZE; i++)
    {
        cout << B[i] << " ";
    }
    cout << "\n==============================\n";
}

//===============================================
// MAIN
//===============================================
int main()
{
    // Note: in the pseudocode, A and B indeces start at 1
    
    // A: input array with unsorted values
    //int A[SIZE] = {2, 5, 3, 0, 2, 3, 0, 3};
    int A[SIZE] = {5, 4, 3, 2, 1, 0, 0, 0};// 0 1 1 1 2 4 4 5
    
    // B: output array with sorted values
    int B[SIZE] = {-1, -1, -1, -1, -1, -1, -1, -1};
    
    int k = 5;// max value of any element in A
    
    // Call counting sort procedure
    counting_sort(A, B, k);
    
    return 0;
}
