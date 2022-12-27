// Insertion sort
#include <iostream>

using namespace std;

const int M = 5;
const int N = 10;


template <typename T> void printArray(T A[], int length)
{
    cout << "Array:\n";
    
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << " ";
    }
    
    cout << endl;
}


template <typename T> void insertionSort(T A[], int length)
{
    /* Generic insertion sort. */
    for (int i = 1; i < length; i++)
    {
        T key = A[i];
        int j = i;
        
        while (j > 0 && A[j-1] > key)
        {
            // insert the A[i] into the sorted subarray A[0...i-1] by swapping
            swap(A[j], A[j-1]);
            j--;
        }
    }
}


int main()
{
    int array1[5] = {7, 2, 8, 5, 4};
    int array2[10] = {4, 5, 6, 8, 1, 2, 3, 5, 4, 7};
    
    insertionSort(array1, M);
    printArray(array1, M);
    
    insertionSort(array2, N);
    printArray(array2, N);
    
    return 0;
}
