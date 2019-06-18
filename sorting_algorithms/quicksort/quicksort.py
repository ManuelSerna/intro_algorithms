#************************************************
'''
    Quicksort

    Best-case time: Theta(n*lg n)
    Worst-case time: Theta(n^2)

    Note: verbose shortened to v
'''
#************************************************
def partition(A, p, r, v):
    x = A[r]
    i = p - 1
    if v:
        print('partitioning')
        print('pivot: ', x)
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            if v:
                print('\t A: ', A)
                print('\t switched {} with {}'.format(A[j], A[i]))
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    if v:
        print('A:', A)
    return i+1

def quicksort(A, p, r, v):
    if p < r:
        q = partition(A, p, r, v)
        quicksort(A, p, q-1, v)
        quicksort(A, q+1, r, v)

#=================================================
# test quicksort
#=================================================
verbose = True
A = [2, 8, 7, 1, 3, 5, 6, 4] # example from section 7.1
#A = [1, 2, 3, 4, 5, 6, 7, 8] # example of worst-case

print('unsorted array: ', A)
quicksort(A, 0, len(A)-1, verbose)
print('final sorted array: ', A)