#************************************************
# Dynamic Programming- rod cutting problem. 
#************************************************

def max(a, b):
    if a > b:
        return a
    else:
        return b

def init_array(r, n):
    for i in range(n):
        r.append(-9999)

#------------------------------------------------
# Top-down approach
#------------------------------------------------
def memoized_cut_rod(p, n):
    # Let r[0..n] be a new array (and initialize)
    r = []
    init_array(r, n)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n-1] >= 0:
        return r[n-1] # desired value known
    if n == 0:
        q = 0 # bottom out
    else:
        q = -9999
        for i in range(1, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n-1] = q # store max profit
    return q

#------------------------------------------------
# Extended bottom-up approach
#------------------------------------------------
'''
def extended_bottom_up_cut_rod(p, n):
    # Let r[0..n] and s[0..n] be new arrays
    r = []
    init_array(r, n)
    s = []
    init_array(s, n)

    r[0] = 0

    for j in range(n):
        q = -9999
        for i in range(j):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return (r, s)

def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n-1])
        n = n - s[n-1]
'''
#================================================
# MAIN
#================================================
#p = [0, 2, 5, 7, 3, 5, 1, 6, 5, 6, 1]
p = [0, 1, 2, 2, 1]
n = len(p) # length of array p

# Top-down call
print("Max value: ", memoized_cut_rod(p, n))

# Bottom-up call
#print_cut_rod_solution(p, n)
