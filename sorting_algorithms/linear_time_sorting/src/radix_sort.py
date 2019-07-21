#************************************************
'''
    Radix sort

    Best-case time: Theta(d(n + k))
    Worst-case time: Theta(d(n + k))
'''
#************************************************

# Get a digit of a number n by performing integer division by a power d (digit) of 10 to get the desired digit in the one's place, then mod 10 to get remainder
# For out-of-range digits, it will return 0
def get_digit(n, d):
    return (n//10**d)%10

#================================================
# Take input array A and extract list of digits
#================================================
def get_digits(A, d):
	D = []
	for i in range(0, len(A)):
		D.append((A[i]//10**d)%10)
	return D

#================================================
'''
	Stable sort: modified counting sort

	Arrays
	A = input array from user
	B = will contain the sorted sequence of elements in A after stable sort is done, values are then copied back to A
	C = auxillary array to perform work as in original counting sort

	Verbose arrays
	D = digits on current d
	S = sorted digits list
'''
#================================================
def counting_sort(A, D, k, verbose):
	B = []
	for i in range(len(A)):
		B.append(-1)
	if verbose:
		S = []
		for i in range(len(A)):
			S.append(-1)
	k += 1
	C = []
	for i in range(k):
		C = C + [0]
	for j in range(0, len(D)):
		C[D[j]] += 1
	for i in range(1, k):
		C[i] += C[i-1]
	for j in range(len(D)-1, -1, -1):
		B[C[D[j]]-1] = A[j]
		if verbose:
			S[C[D[j]]-1] = D[j]
		C[D[j]] -= 1
	for i in range(len(A)):
		A[i] = B[i] # copy data from temp array
	if verbose:
		print('A sorted on current digit:', A)
	
#================================================
# Radix sort
#================================================
def radix_sort(A, digits, verbose):
	if verbose:
		print('input: ', A)
	for digit in range(0, digits):
		D = get_digits(A, digit)
		k = max(D)
		if verbose:
			print('k = {} for digit {}\n\tdigit list: {}'.format(k, digit, D))
		counting_sort(A, D, k, verbose)
	print('final sorted array: ', A)

#================================================
# Test radix sort
#================================================
A = [329, 457, 657, 839, 436, 720, 355] # example from figure 8.3
d = 3
verbose = True
radix_sort(A, d, verbose)
