#************************************************
'''
    Counting sort

    Best-case time: Theta(n + k)
    Worst-case time: Theta(n + k)
'''
#************************************************
def counting_sort(A, B, k, verbose):
	k += 1 # account for zero
	C = []
	for i in range(k):
		C = C + [0] # extend C to be length k+1 and intialize
	for j in range(0, len(A)):
		C[A[j]] += 1
	# C[i] now contains the number of elements equal to i
	if verbose:
		print('max number k: ', k-1)
		print('unsorted input array A: ', A)
		print('C where C[i] contains the number of elements equal to i:', C)
	for i in range(1, k):
		if verbose:
			print('\ti: ', i)
			print('\tC: ', C)
		C[i] += C[i-1]
	# C[i] now contains the number of elements less than or equal to i
	if verbose:
		print('C where C[i] contains the number of elements less less than or equal to i: ', C)
		print('\n*Now placing elements in sorted order*\n')
	for j in range(len(A)-1, -1, -1):
		if verbose:
			print(
				'placing {} into index={} of B'
				.format(A[j], C[A[j]]-1)
			)
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1
		if verbose:
			print('B: ', B, '\n')

#================================================
# test counting sort
#================================================
A = [2, 5, 3, 0, 2, 3, 0, 3]
B = []
for i in range(len(A)):
	B.append(-1)
k = 5
verbose = True

counting_sort(A, B, k, verbose)
print('final sorted array: ', B)
