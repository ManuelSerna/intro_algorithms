//***********************************************
// Quick sort algorithm implementation
/*
    Best case run time: Theta(n lg n)
    Worst case run time: Theta(n^2)
*/
//***********************************************
#include <iostream>
using namespace std;

const int SIZE = 8;

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

//-----------------------------------------------
/*
    Partition function used for quick sort.
    Inputs:
            A --array to be sorted.
            p --left
    Notes:
            A[0...i] --subarray whose elements are less than pivot.
            A[i
*/
//-----------------------------------------------
int partition(int A[], int p, int r)
{
    cout << endl;
    cout << "Partitioning." << endl;
    
    int x = A[r];
    int i = p-1;
    
    cout << "Pivot: " << x << endl;

    // Compare pivot value x from p until before x 
    for(int j = p; j < r; j++)
    {
        if(A[j] <= x)
        {
            i++;// increase size of left partition

            // Exchange A[i] with A[j]
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;

            print(A, SIZE);
            cout << "\t--switched " << A[j] << " with " << A[i] << endl;
            cout << "--------------------------------" << endl;;
        }
    }

    // Place current pivot after left subarray A[i+1].
    // Now, we have a new pivot for right subarray A[i+2...r].
    int temp = A[i+1];
    A[i+1] = A[r];
    A[r] = temp;

    print(A, SIZE);
    cout << "================================\n";

    return i + 1;
}

//-----------------------------------------------
// Quick sort algorithm
//-----------------------------------------------
void quicksort(int A[], int p, int r)
{
    if(p < r)
    {
        // Keep partitioning until recursion bottoms out.
        int q = partition(A, p, r);
        quicksort(A, p, q-1);
        quicksort(A, q+1, r);
    }
}

//-----------------------------------------------
// MAIN
//-----------------------------------------------
int main()
{
    // Random data (best case: n*log base 2 of n)
    int A[SIZE] = {2, 8, 7, 1, 3, 5, 6, 4};

    // Worst case: already sorted data (n^2 time)
    //int A[SIZE] = {1, 2, 3, 4, 5, 6, 7, 8};

    // Sort A using quicksort
    quicksort(A, 0, SIZE-1);

    cout << "Sorted array: " << endl;
    print(A, SIZE);
    cout << endl;

    return 0;
}
