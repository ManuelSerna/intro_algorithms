#************************************************
'''
    Heapsort and Priority Queue

    Any case run time for heapsort: O(n*lg n)
'''
#************************************************

neg_infty = -999999


def swap(array:list = None, i:int = None, j:int = None) -> None:
    """ Swap elemets indexed by i and j in array 'array'. """
    temp = array[i]
    array[i] = array[j]
    array[j] = temp



class Heap():
    #--------------------------------------------
    def __init__(self, array:list = None):
        self.heap = [0]
        self.heap_size = 0 # keeps track of real heap size

        if array is not None:
            self.heap += array # append zero to make heap 1-based
            self.heap_size = len(array)


    #--------------------------------------------
    # Getters for chilren and parent node locations (for zero-based arrays)
    # Running time: Theta(1)
    #--------------------------------------------
    def parent(self, i) -> int:
        return i//2

    def left(self, i) -> int:
        return (2*i)

    def right(self, i) -> int:
        return (2*i) + 1

    #--------------------------------------------
    # Max heapify (recursive) array "nodes"
    # Running time: Theta(lg n)
    #--------------------------------------------
    def max_heapify(self, i:int) -> None:
        l = self.left(i)
        r = self.right(i)
        largest = 0

        if l <= self.heap_size and self.heap[l] > self.heap[i]:
            largest = l # largest val is left child
        else:
            largest = i

        if r <= self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r # largest val is right child

        # If largest value is either child, go down that path of the heap
        if largest != i:
            swap(self.heap, i, largest)
            self.max_heapify(largest)

    #--------------------------------------------
    # Build a max heap
    # Runnint time: O(n)
    #--------------------------------------------
    def build_max_heap(self):
	    for i in range(self.heap_size//2 + 1, 0, -1):
		    self.max_heapify(i)

    #--------------------------------------------
    # Heapsort array "nodes"
    # Running time: O(n lg n)
    #--------------------------------------------
    def heapsort(self):
	    self.build_max_heap()
	    length = self.heap_size
	    
	    for i in range(length, 1, -1):
		    swap(self.heap, 1, i)
		    self.heap_size -= 1
		    self.max_heapify(1)

    #--------------------------------------------
    # Heap max
    #--------------------------------------------
    def heap_maximum(self):
        return self.heap[1]

    #--------------------------------------------
    # Heap extract max
    # Get root value and re-max-heapify using last value in heap
    #--------------------------------------------
    def heap_extract_max(self):
	    if self.heap_size < 1:
		    raise Exception('heap underflow')
	    
	    max_val = self.heap[1]
	    
	    self.heap[1] = self.heap[self.heap_size+1] # account for zero-element
	    self.heap_size -= 1
	    self.max_heapify(1)
	    
	    return max_val

    #--------------------------------------------
    # Heap increase key
    #--------------------------------------------
    def heap_increase_key(self, i, key):
	    if key < self.heap[i]:
		    raise Exception('new key is smaller than current key')
	    
	    self.heap[i] = key
	    
	    # Keep going up the heap as we push the larger children's value up
	    while i > 1 and (self.heap[self.parent(i)] < self.heap[i]):
		    swap(self.heap, self.parent(i), i)
		    i = self.parent(i)

    #--------------------------------------------
    # Max-heap insert
    #--------------------------------------------
    def max_heap_insert(self, key):
	    self.heap_size += 1
	    self.heap.append(neg_infty) # grow heap by appending to list
	    self.heap_increase_key(self.heap_size, key)

    #--------------------------------------------
    # Heap delete
    #--------------------------------------------
    def heap_delete(self, i):
	    swap(self.heap, self.heap_size, i)

	    del self.heap[self.heap_size] # delete last item in list
	    A.heap_size -= 1

        # Now, adjust heap based on whether...
	    if self.heap[i] > self.heap[self.parent(i)]:
		    self.heap_increase_key(i, self.heap[i]) # value needs to move up heap
	    else:
		    self.max_heapify(i) # value needs to move down heap

    #--------------------------------------------
    # Print
    #--------------------------------------------
    def print(self):
	    print(self.heap)

#================================================
# Test
#================================================
array1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
array2 = [25, 16, 5, 9, 12, 3, 2, 8] # already a max heap, albeit a weird one

print("First array")
A = Heap(array1)

A.build_max_heap()
A.print()

A.max_heap_insert(17)
print("After inserting value: 17")
A.print()

A.heap_delete(5) # delete value 14 at i=5, value 7 moves up, done.
print("After deleting i=5 (value 14)")
A.print()
A.heap_delete(4) # delete value 8 at i=4, max heapify on i=4 to get value 4, done.
print("After deleting i=4 (value 8)")
A.print()

A.heapsort()
print('sorted A array: ')
A.print()

print('\nSecond array')

# Heap B will showcase different behavior when deleting
B = Heap(array2)
B.build_max_heap()
print("After building a max heap:")
B.print()

B.heap_delete(7) # delete value 2 at i=7, use increase-key to propagate value 8 up, done.
print("After deleting i=7 (value 2)")
B.print()
