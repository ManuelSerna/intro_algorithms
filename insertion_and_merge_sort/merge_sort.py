#************************************************
# Merge sort algorithm.
'''
    Theta(n lg n) runtime in avg and worst case.
    Theta(n) runtime in best case.
'''
#************************************************
import sys

def merge_sort(A, p, r):
    if p < r:
        q = int((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        
#------------------------------------------------------
# Merge procedure: Theta(n) runtime.
#------------------------------------------------------
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    #L = Array(n1)
    #R = Array(n2)
    L = []
    R = []

    for x in range(1,len(L)):
        L[x] = A[p + x - 1]
    for x in range(1,len(R)):
        R[x] = Af[q + x]

    # Add sentinel values
    #R[len(R)] = float("inf")
    #L[len(L)] = float("inf")
    R[len(R)] = sys.maxsize
    L[len(L)] = sys.maxsize

    j = 1
    i = 1
    
    print("L: ", L)
    print("R: ", R)

    for x in range(p,r+1):
        if L[i] <= R[j]:
            A[x] = L[i]
            print(A)
            i = i + 1
        
        elif R[j] < L[i]:
            A[x] = R[j]
            print(A)
            j = j+1
            
#================================================
# Test
#================================================
A = [4, 5, 6, 8, 1, 2, 3, 5, 4, 7]
merge_sort(A, 0, len(A))
