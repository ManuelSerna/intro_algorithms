"""
Below are the following 'bad' sorts:
* Bubble sort
    - This algorithm iterates through all positions in the array. 
      For each position i in the array, we bring to position i the i-th smalleset element,
      hence the second for loop starting from the last position in A.
      We check A[j-1] > A[j] and if it's true, swap since the elements are out of order
      (we want to make sure A[j-1] < A[j], naturally by def. of sorting).
    - Worst case runtime is O(n^2) due to the double for loop occuring regardless of input.

* Insertion sort
    - Intuitively, this is like having a set of playing cards in your hand, and we draw a card,
      and then we insert the drawn card into its sorted position in our hand.
      In insertion sort, we have a growing subarray which contains our sorted inputs starting 
      from index i=0. When we insert a new element into the sorted subarray, we go down the array,
      comparing with each element as we go until we are in a sorted position.
    - NOTE: Insertion sort is good at handling small inputs as opposed to other sorting
      algorithms (e.g., quicksort and merge sort). The other sorting algorithms have more
      overhead, hence their relative slowness in handling smaller inputs.
    - Worst-case runtime is O(n^2).
    - Best-case runtime is O(n) since we may not enter the while loop.

* Selection sort
    - This algorithm goes through the entire array and inserts the smallest element at 
      A[0]. Then it searches the remaining--unsorted part of the array for the second-
      smallest element, and inserts it at A[1], and so on.
    - Generally this performs worse than insertion sort.
    - Worst-case runtime is O(n^2).
"""

def bubble_sort(A:list=None, verbose:bool=False) -> None:
    N = len(A)

    for i in range(N):
        if verbose:
            print(f"i={i} up to {N-1}")
        
        for j in range(N-1, i, -1):
            if verbose:
                print(f"...j={j}")

            if A[j-1] > A[j]:
                # swap larger element in pos j-1 & pos j
                tmp = A[j-1]
                A[j-1] = A[j]
                A[j] = tmp

                if verbose:
                    print(f">{A}")

def insertion_sort(A:list=None, verbose:bool=False) -> None:
    for i in range(1,len(A)):
        if verbose:
            print(f"i={i} up to {len(A)-1}")

        key = A[i]
        j = i-1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

            if verbose:
                print(A)

        A[j+1] = key

        if verbose:
            print(A)

def insertion_sort2(A:list=None) -> None:
    """ A more intuitive version of Insertion Sort.
    
    This is not as optimized as the first version, but
    it is closer to how people would do it on paper.

    for i=1 up to N:
        j = i-1
        while j >= 0 and A[j] > A[j+1]:
            swap(A[j], A[j+1])
            j--
    """
    print("Calling insertion sort 2")

    for i in range(1, len(A)):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            # swap(A[j], A[j+1])
            tmp = A[j]
            A[j] = A[j+1]
            A[j+1] = tmp

            j -= 1
            print(A)

def selection_sort(A:list=None, verbose:bool=False) -> None:
    for i in range(len(A)-1):
        idx = i

        for j in range(i+1, len(A)):
            if A[j] < A[idx]:
                idx = j

        if verbose:
            print(f"...i={i}: smallest={idx}, A[{idx}]={A[idx]}")

        # swap smallest and A[i], now sorted subarray grows by one
        tmp = A[i]
        A[i] = A[idx]
        A[idx] = tmp

        if verbose:
            print(A)

def main() -> None:
    A = [5,4,8,1,7,9,5,1,2,5,3,7,2,8]
    #A = [5,2,7,1,6,3]
    print(A)
    bubble_sort(A, True)
    print(A)

    B = [5,4,8,1,7,9,5,1,2,5,3,7,2,8]
    #B = [5,2,7,1,6,3]
    #B=[81,13,77,24,35,61,48,3,23,87,92,95,74,57,99,86,28,15,55,7,51]
    print(B)
    #insertion_sort(B, True)
    insertion_sort2(B)
    print(B)

    C = [5,4,8,1,7,9,5,1,2,5,3,7,2,8]
    #C = [3,2,5,8,7,6]
    print(C)
    selection_sort(C, True)
    print(C)

if __name__ == "__main__":
    main()
