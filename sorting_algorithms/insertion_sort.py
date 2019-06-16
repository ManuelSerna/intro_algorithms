#************************************************
'''
    Insertion Sort

    Best case run time: Theta(n)
    Worst case run time: Theta(n^2)
'''
#************************************************

def insertion_sort(A, verbose):
    if verbose: 
        print('Starting array: ',A, '\n')
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1..j]
        i = j - 1 # start at the end of the sorted sequence
        while i >= 0 and A[i] > key:
            if verbose: 
                print('  Moving key={} from j={} into sorted subsequence of A: {}'.format(key, j, A))
            A[i+1] = A[i] # shift actual values in the sorted subsequence up
            i = i - 1 # shift index for subsequence too
            if verbose:
                print('  After shifting: ', A)
        A[i+1] = key # insert new value in proper place
        if verbose: 
            print('    Inserted key={} into index={}, with A: {}\n'.format(key, i+1, A))
    print('\nFinal sorted array: ', A)


#================================================
# Sort some test arrays
#================================================
A = [7, 2, 8, 5, 4] # example from notes
B = [4, 5, 6, 8, 1, 2, 3, 5, 4, 7] # gnarly
verbose = True

insertion_sort(A, verbose)

#insertion_sort(B, verbose)
