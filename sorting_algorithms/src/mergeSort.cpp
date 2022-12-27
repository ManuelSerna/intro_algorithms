#include <iostream>

using namespace std;

const int M = 5;
const int N = 10;


template <typename T> void printArray(T A[], int startIdx, int endIdx)
{
    cout << "Array: ";
    for (int i = startIdx; i <= endIdx; i++) { cout << A[i] << " "; }
    cout << endl;
}

template <typename T> T* createSubArray(T inputArray[], int startIdx, int endIdx)
{
    /* 
    Dynamically allocate new array so we can work with it outside this function
    ...remember to de-allocate with: 
        delete[] subarray;
    */
    int length = endIdx - startIdx + 1;
    int i = startIdx;// index for input array
    int j = 0;// index for sub array
    
    T* subarray = new T[length];
    
    while (i <= endIdx)
    {
        subarray[j] = inputArray[i];
        i++;
        j++;
    }
    
    return subarray;
}


template <typename T> void mergeSort(T A[], int startIdx, int endIdx)
{
    /* Generic merge sort */
    int length = endIdx - startIdx + 1;
    
    if (length > 1)
    {
        // Keep splitting array if we have more than one element
        int splitIdx = length / 2;
        
        T* L = createSubArray(A, startIdx, splitIdx-1); // copy left elements
        T* R = createSubArray(A, splitIdx, endIdx); // copy right elements
        
        mergeSort(L, 0, splitIdx-1-startIdx); // process left subarray
        mergeSort(R, 0, endIdx-splitIdx); // process right subarray
        
        // Merge...
        int lenL = splitIdx-1-startIdx+1;
        int lenR = endIdx-splitIdx+1;
        
        int i = 0;// track elements in L
        int j = 0;// track elements in R
        int k = 0;// track elements in A
        
        while (i < lenL && j < lenR)
        {
            // Insert smallest from either L or R until either one is entirely processed
            if (L[i] < R[j])
            {
                A[k] = L[i];
                i++;
            }
            else
            {
                A[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < lenL)
        {
            // Insert remaining elements from L, if any
            A[k] = L[i];
            i++;
            k++;
        }
        while (j < lenR)
        {
            // Insert remaining elements from R, if any
            A[k] = R[j];
            j++;
            k++;
        }
        
        // Cleanup
        delete[] L;
        delete[] R;
    }
}


int main()
{
    int A[M] = {7, 2, 8, 5, 4};
    int B[N] = {4, 5, 6, 8, 1, 2, 3, 5, 4, 7};
    
    printArray(A, 0, M-1);
    mergeSort(A, 0, M-1);
    printArray(A, 0, M-1);
    
    printArray(B, 0, N-1);
    mergeSort(B, 0, N-1);
    printArray(B, 0, N-1);
}
