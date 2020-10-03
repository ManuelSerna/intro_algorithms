//********************************
// Quicksort for C++
// NOTE: when calling functions, high must be subtracted by 1 (I should fix this)
// Functions for both integers and strings
//********************************
#include <iostream>
#include <string>

using namespace std;

// Integer quicksort
int partition(int A[], int low, int high)
{
    int x = A[high];
    int i = low-1;
    
    for (int j=low; j<high; j++)
    {
        if (A[j] <= x)
        {
            i++;
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    }
    
    int temp = A[i+1];
    A[i+1] = A[high];
    A[high] = temp;
    
    return i+1;
}

void quicksort(int A[], int low, int high)
{
    if (low < high)
    {
        int q = partition(A, low, high);// assign partition element to index q
        quicksort(A, low, q-1);
        quicksort(A, q+1, high);
    }
}

// String version of quicksort
int partitionStr(string A[], int low, int high)
{
    string x = A[high];
    int i = low-1;
    
    for (int j=low; j<high; j++)
    {
        if (A[j] <= x)
        {
            i++;
            string temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    }
    
    string temp = A[i+1];
    A[i+1] = A[high];
    A[high] = temp;
    
    return i+1;
}

void quicksortStr(string A[], int low, int high)
{
    if (low < high)
    {
        int q = partitionStr(A, low, high);// assign partition element to index q
        quicksortStr(A, low, q-1);
        quicksortStr(A, q+1, high);
    }
}


// Test code
int main()
{
	// Test integers
	int nums[] = {5, 28, 9, 1 , 4, 22, 9, 5, 56, 76};

	for (int i=0;i<10;i++)
		cout << nums[i] << " ";
	cout << endl;
	quicksort(nums, 0, 10-1);
	for (int i=0;i<10;i++)
		cout << nums[i] << " ";
	cout << endl;
    
    // Test strings
	const int SIZE_2 = 10;
	string data2[SIZE_2] = {"idiom", "car", "fish", "dandy", "seven", "time", "ate", "eat", "man", "joe"};// sorted: ate, caro, dandy, eat, fish,  idiom, john, manuel, seven, time

	for (int i=0;i<SIZE_2;i++)
		cout << data2[i] << " ";
	cout << endl;
    quicksortStr(data2, 0, SIZE_2-1);
	for (int i=0;i<SIZE_2;i++)
		cout << data2[i] << " ";
	cout << endl;

	return 0;
}
