#************************************************
'''
    Merge sort

    Any case run time: Theta(n*lg n)
'''
#************************************************
def merge_sort(A, verbose):
    if len(A) > 1:
        # Split array in half via integer/floor division
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        if verbose: print("left partition: ", L, ", right partition: ", R)

        # Keep splitting sub arrays until arrays are of size 1. This process takes Theta(lg n) time.
        merge_sort(L, verbose)
        merge_sort(R, verbose)

        if verbose:
            print("left array:  ", L)
            print("right array: ", R)
        
        # Initialize indices for...
        i = 0 # index to keep track of values in L
        j = 0 # index to keep track of values in R
        k = 0 # index to insert sorted values into A
        
        # Copy data from L[i] or R[j] to A[k].
        # See which value in L and R is smaller, insert that smaller element into A. This process takes Theta(n) time.
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
            if verbose: print("inserting", A[k], "into array", A)
        
        # Copy any remaining elements to A, obviously from smaller (L) to bigger (R)
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    if verbose: print("sorted array: ", A)

#================================================
# Sort some test arrays.
#================================================
A = [7, 2, 8, 5, 4]
B = [4, 5, 6, 8, 1, 2, 3, 5, 4, 7]
verbose = True

merge_sort(A, verbose)
