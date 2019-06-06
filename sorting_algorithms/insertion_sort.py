#************************************************
'''
	Insertion Sort
	
	Best case run time: Theta(n)
	Worst case run time: Theta(n^2)
'''
#************************************************

def insertion_sort(A, verbose):
	if verbose: print(A)
	for j in range(1, len(A)):
		key = A[j]

		# Insert A[j] into the sorted sequence A[1..j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
			if verbose: print(A)
		A[i+1] = key
		if verbose: print(A)


#================================================
# Sort some test arrays
#================================================
A = [7, 2, 8, 5, 4]
B = [4, 5, 6, 8, 1, 2, 3, 5, 4, 7]
verbose = True

insertion_sort(A, verbose)
