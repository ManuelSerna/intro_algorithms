#************************************************
# Insertion sort aglorithm
'''
    Best case run time: Theta(n)
    Worst case run time: Theta(n^2)
'''
#************************************************

def insertion_sort(A):
    for j in range(1, len(A)):
        # 
        key = A[j]
        
        # Insert A[j] into the sorted sequence A[1...j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    
#------------------------------------------------
# Sort some array A.
#------------------------------------------------

A = [4, 5, 6, 8, 1, 2, 3, 5, 4, 7]
print("Unsorted array: ", A)
insertion_sort(A)
print("Sorted array: ", A)
