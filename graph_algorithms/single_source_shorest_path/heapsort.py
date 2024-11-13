neg_infty = -999999


def swap(array:list = None, i:int = None, j:int = None) -> None:
    """ Swap elemets indexed by i and j in array 'array'. """
    temp = array[i]
    array[i] = array[j]
    array[j] = temp



class Heap():
    #--------------------------------------------
    def __init__(self, array:list = None):
        self.heap = [None]
        self.heap_size = 0 # keeps track of real heap size

        if array is not None:
            self.heap += array # append zero to make heap 1-based
            self.heap_size = len(array)
            #for i in range(1, len(self.heap)):
            #    self.heap[i].d *= -1

    #--------------------------------------------
    # Return boolean whether there are no elements in the heap
    #--------------------------------------------
    def is_empty(self):
        return self.heap_size == 0

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

        if l <= self.heap_size and self.heap[l].d > self.heap[i].d:
            largest = l # largest val is left child
        else:
            largest = i

        if r <= self.heap_size and self.heap[r].d > self.heap[largest].d:
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
    # Heap *min*
    #--------------------------------------------
    def heap_maximum(self):
        return self.heap[1] * -1 # make sure to return min

    #--------------------------------------------
    # Heap extract max
    # Get root value and re-max-heapify using last value in heap
    #--------------------------------------------
    def heap_extract_max(self):
        if self.heap_size < 1:
            raise Exception('heap underflow')
	    
        max_val = self.heap[1]
        
        # Replace Vertex object reference
        self.heap[1] = self.heap[self.heap_size] # account for zero-element
        self.heap_size -= 1
        self.max_heapify(1)

        return max_val

    #--------------------------------------------
    # Heap increase key
    # ...increase distance attribute
    #--------------------------------------------
    def heap_increase_key(self, i, key):
	    if key < self.heap[i].d:
		    raise Exception('new key is smaller than current key')
	    
	    #self.heap[i].distance = -1*key
	    
	    # Keep going up the heap as we push the larger children's value up
	    while i > 1 and (self.heap[self.parent(i)].d < self.heap[i].d):
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
	    if self.heap[i].d > self.heap[self.parent(i)].d:
		    self.heap_increase_key(i, self.heap[i]) # value needs to move up heap
	    else:
		    self.max_heapify(i) # value needs to move down heap

    #--------------------------------------------
    # Print
    #--------------------------------------------
    def print(self):
	    #print(self.heap)
        for i in range(1, len(self.heap)):
            print(f"{i}: {self.heap[i].d}")

