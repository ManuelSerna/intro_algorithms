#************************************************
'''
    Heapsort and Priority Queue

    Any case run time for heapsort: O(n*lg n)
'''
#************************************************

neg_infty = -999999

class Heap():
	#--------------------------------------------
	def __init__(self, array):
		self.length = len(array)
		self.heap_size = 0
		self.nodes = [0] + array # append zero to make heap 1-based

	#--------------------------------------------
	# Getters for chilren and parent node locations (for zero-based arrays)
	# Running time: Theta(1)
	#--------------------------------------------
	def parent(self, i):
	    return i//2

	def left(self, i):
	    return (2*i)

	def right(self, i):
	    return (2*i) + 1

	#--------------------------------------------
	# Max heapify (recursive) array "nodes"
	# Running time: Theta(h) for height of a node h = lg n
	#--------------------------------------------
	def max_heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		largest = 0
		if l <= self.heap_size and self.nodes[l] > self.nodes[i]:
			largest = l
		else:
			largest = i
		if r <= self.heap_size and self.nodes[r] > self.nodes[largest]:
			largest = r
		if largest != i:
			temp = self.nodes[i]
			self.nodes[i] = self.nodes[largest]
			self.nodes[largest] = temp
			self.max_heapify(largest)

	#--------------------------------------------
	# Build a max heap
	# Runnint time: O(n)
	#--------------------------------------------
	def build_max_heap(self):
		self.heap_size = self.length
		for i in range(self.length//2, 0, -1):
			self.max_heapify(i)

	#--------------------------------------------
	# Heapsort array "nodes"
	# Running time: O(n lg n)
	#--------------------------------------------
	def heapsort(self):
		self.build_max_heap()
		for i in range(self.length, 1, -1):
			temp = self.nodes[1]
			self.nodes[1] = self.nodes[i]
			self.nodes[i] = temp
			self.heap_size -= 1
			self.max_heapify(1)

	#--------------------------------------------
	# Heap max
	#--------------------------------------------
	def heap_maximum(self):
	    return self.nodes[1]

	#--------------------------------------------
	# Heap extract max
	#--------------------------------------------
	def heap_extract_max(self):
		if self.heap_size < 1:
			raise Exception('heap underflow')
		max_ = self.nodes[1]
		self.nodes[1] = self.nodes[self.heap_size]
		self.heap_size -= 1
		self.max_heapify(1)
		return max_

	#--------------------------------------------
	# Heap increase key
	#--------------------------------------------
	def heap_increase_key(self, i, key):
		if key < self.nodes[i]:
			raise Exception('new key is smaller than current key')
		self.nodes[i] = key
		while i > 1 and (self.nodes[self.parent(i)] < self.nodes[i]):
			temp = self.nodes[i]
			self.nodes[i] = self.nodes[self.parent(i)]
			self.nodes[self.parent(i)] = temp
			i = self.parent(i)

	#--------------------------------------------
	# Max-heap insert
	#--------------------------------------------
	def max_heap_insert(self, key):
		self.heap_size += 1
		self.length += 1
		self.nodes.append(neg_infty) # grow heap by appending to list
		self.heap_increase_key(self.heap_size, key)

	#--------------------------------------------
	# Heap delete
	#--------------------------------------------
	def heap_delete(self, i):
		temp = self.nodes[i]
		self.nodes[i] = self.nodes[self.heap_size]
		self.nodes[self.heap_size] = temp

		del self.nodes[self.heap_size] # delete from heap by deleting last item in list
		A.heap_size -= 1
		self.length -= 1

		if self.nodes[i] > self.nodes[self.parent(i)]:
			self.heap_increase_key(i, self.nodes[i])
		else:
			self.max_heapify(i)

	#--------------------------------------------
	# Print
	#--------------------------------------------
	def print(self):
		print(self.nodes)

#================================================
# Test
#================================================
array1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
array2 = [25, 16, 5, 9, 12, 3, 2, 8] # already a max heap, albeit a weird one

A = Heap(array1)

A.build_max_heap()
A.print()

A.max_heap_insert(17)
A.print()

A.heap_delete(5) # delete value 14 at i=5, value 7 moves up, done.
A.heap_delete(4) # delete value 8 at i=4, max heapify on i=4 to get value 4, done.
A.print()

A.heapsort()
print('sorted A array: ', A.nodes)

print('\nsecond array')

# Heap B will showcase different behavior when deleting
B = Heap(array2)
B.build_max_heap()
B.print()

B.heap_delete(7) # delete value 2 at i=7, use increase-key to propagate value 8 up, done.
B.print()
