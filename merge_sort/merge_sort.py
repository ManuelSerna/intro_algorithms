#************************************************
# Merge sort algorithm.
# Any case run time: Theta(n lg n)
#************************************************
def merge_sort(A):
    if len(A) > 1:
        # Find middle of array
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        
        # Keep splitting sub arrays.
        # This process takes Theta(lg n) time.
        merge_sort(L)
        merge_sort(R)
        
        # Initialize indices for 
        i = 0
        j = 0
        k = 0
        
        #Copy data from L[j] or R[i] to A[k].
        #See which value in L and R is smaller, insert that smaller element into A. This process takes Theta(n) time.
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        
        # Copy any remaining elements to A. Start with L.
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

#================================================
# Test merge sort.
#================================================

A = [4, 8, 5, 7, 1, 6, 3, 2]
print("Unsorted array: ", A)
merge_sort(A)
print("Sorted array: ", A)
