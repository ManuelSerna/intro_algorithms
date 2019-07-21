#************************************************
'''
    Bucket sort

    Best-case time: Theta(n)
    Worst-case time: Theta(n^2) using insertion sort
'''
#************************************************
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
        
def bucket_sort(A, verbose):
	n = len(A)
	# let B[0..n-1] be a new array
	B = []
	for i in range(n):
		B = B + [[]] # add empty lists
	if verbose:
		print('empty list B: ', B)

	for i in range(n):
		B[int(n*A[i])].append(A[i])
	if verbose:
		print('unsorted buckets: ', B)

	for i in range(n):
		insertion_sort(B[i])
	if verbose:
		print('sorted buckets: ', B)

	# Concatenate non-empty lists to S
	S = []
	for i in range(n):
		if B[i] != None:
			for j in range(len(B[i])):
				S.append(B[i][j])
	if verbose:
		print('final sorted array S: ', S)

#================================================
# Test bucket sort
#================================================
A = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68] # example from figure 8.4
verbose = True
bucket_sort(A, verbose)