"""
Give an algorithm that, given n integers in the range [0, k], preprocesses 
its input and then answers how many of the n integers fall into the range
[a...b] in O(1) (i.e., constant) time. You are allowed Theta(n+k) 
preprocessing time.
"""
from copy import deepcopy

def counting_sort(A:list, _k:int) -> list:
    """ Counting Sort

    This algorithm assumes that the inputs are integers that fall
    into the range [0,k]. Given the length of A is n, the algorithm 
    will always run in O(n+k) (either n or k will dominate the runtime).
    """
    # Setup
    k = _k+1 # account for 0
    B = [-1 for i in range(len(A))]
    C = [0 for i in range(k)]

    # Count
    for i in range(len(A)):
        C[A[i]] += 1
    #counts = deepcopy(C)

    # Perform inclusive scan s.t. C[i] contains elements <=C[i]
    for i in range(1, k):
        C[i] += C[i-1]
    scan = deepcopy(C)

    # Placement
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B, scan

def find_num_in_sorted_range(array:list, start:int, end:int) -> int:
    """ Find how many integers fall into the closed range
    [start, end]

    and to do this we use the counting sort algorithm's inclusive scan
    array that we get just before we actually do the sorting.

    The arg 'array' is a list where array[i] contains the number of
    elements less than or equal to array[i].

    This function runs in constant time.
    """
    if start == 0:
        return array[end]
    else:
        return array[end] - array[start-1]

def main():
    # Make up data
    #V = [4,1,3,2,4,5,8,4,1,8,2,7,4,5,0,1,7,5]
    V = [3,3,6,2,0,2,6,1,4,2,0,3,6,2,5,3,0,1,2,6,4,6,6,6]
    Vmin = min(V)
    Vmax = max(V)
    k = Vmax # range [0, k]

    # Counting sort allows us Theta(n+k) preprocessing time
    print('original:')
    print(V)
    array, scan = counting_sort(V, k)
    print('sorted:')
    print(array)
    print('inclusive scan:')
    print(scan)
    print()

    # Query about how many values fall into some [a...b] in constant time
    a = 0
    b = 2
    res = find_num_in_sorted_range(scan, a, b)
    print(f"[{a}...{b}]: {res}")

    a = 2
    b = 5
    res = find_num_in_sorted_range(scan, a, b)
    print(f"[{a}...{b}]: {res}")

if __name__ == "__main__":
    main()
