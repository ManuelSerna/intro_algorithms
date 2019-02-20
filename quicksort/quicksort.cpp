/************************************************
 Quick sort algorithm implementation
************************************************/
#include <iostream>
using namespace std;

const int SIZE = 8;

//-----------------------------------------------
// Partition function used for quick sort.
//-----------------------------------------------
int partition(int A[], int p, int r)
{
    cout << "\nPartitioning." << endl;
    int x = A[r];
    int i = p-1;
    cout << "New pivot value: " << x << endl;

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

            for(int i = 0; i < SIZE; i++)
            {
                cout << "|"<< A[i];
            }
            cout << "|";
            cout << " <- switched " << A[j] << " with " << A[i] << endl;
            cout << "--------------------------------\n";
        }
    }

    // Put pivot at the end of subarray bigger than x
    // -(exchange A[i+1] with A[r])
    int temp = A[i+1];
    A[i+1] = A[r];
    A[r] = temp;// new pivot value for next call for partition

    for(int i = 0; i < SIZE; i++)
    {
        cout << "|"<< A[i];
    }
    cout << "|" << endl;
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
        int q = partition(A, p, r); // recurse again on pivot
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

    quicksort(A, 0, SIZE-1);// sort array using quicksort

    cout << "Sorted array: " << endl;
    for(int i = 0; i < SIZE; i++)
    {
        cout << "|" << A[i];
    }
    cout << "|" << endl;

    return 0;
}
