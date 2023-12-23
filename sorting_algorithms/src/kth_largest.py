"""Get k-th largest element in an array.

In this implementation, use the quicksort partition() function.
"""

def partition(A:list, left:int, right:int) -> int:
    pivot = A[right]
    i = left-1

    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp

    tmp = A[i+1]
    A[i+1] = A[right]
    A[right] = tmp

    return i+1

def quicksort(A:list, left:int, right:int) -> int:
    if left < right:
        m = partition(A, left, right)
        quicksort(A, left, m-1)
        quicksort(A, m+1, right)

def find_k_largest(A:list, k:int):
    left = 0
    right = len(A)-1
    mid = partition(A, left, right)

    while k != mid:
        if k < mid:
            right = mid-1
        elif k > mid:
            left = mid+1
        mid = partition(A, left, right)

    return A[mid]

def main():
    A = [6, 12, 14, 11, 7, 1, 9, 5, 4, 13, 3]
    l = 0
    r = len(A)-1

    k = 0 

    print("Unsorted:")
    print(A)
    res = find_k_largest(A, k)
    print(f"{k}-largest element in array: {res}")
    
    quicksort(A, l, r)
    print("Index:")
    print([i for i in range(len(A))])
    print("Sorted:")
    print(A)


if __name__ == "__main__":
    main()
