#************************************************
# Dynamic Programming Example - matrix-chain multiply (adjusted for zero-based arrays).
#************************************************

infty = 999999

#------------------------------------------------
# Print n*n table t.
#------------------------------------------------
def print_table(t, n, label):
    print('table: ', label)
    for i in range(n):
        print(t[i])

#------------------------------------------------
# Return an n*n table t.
#------------------------------------------------
def make_table(n):
    t = []
    for i in range(n):
        t.append([])
        for j in range(n):
            t[i].append(0)
    return t

#------------------------------------------------
# Find optimal sequence, get back: m AND s.
#------------------------------------------------
def matrix_chain_order(p, verbose):
    n = len(p)-1
    
    m = make_table(n)
    s = make_table(n) # table s used to construct optimal solution
    
    for i in range(n):
        m[i][i] = 0
    
    for l in range(1, n): # l is chain length (n+1)
        for i in range(n-l):
            j = i + l
            m[i][j] = infty
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + (p[i] * p[k+1] * p[j+1])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k+1 # add 1 to adjust for zero-based table
                if verbose:
                    print('q = {} = {} + {} + ({} * {} * {})'.format(q, m[i][k], m[k+1][j], p[i], p[k+1], p[j+1]))
                    print('potential value at m[{}, {}]: {}'.format(i, j, q))
                if verbose:
                    print('updated table m')
                    print_table(m, n, 'm')
                    print('updated table s')
                    print_table(s, n, 's')
            if verbose:
                print()
        if verbose:
            print()
    
    if verbose:
        print('final tables')
        print_table(m, n, 'm')
        print_table(s, n, 's')
    
    print('\noptimal value: ', m[0][n-1])
    return m, s

#================================================
# Test matrix-chain order method.
#================================================

# List of dimensions
#p = [5, 4, 6, 2, 7] # from Mr. Bari's example
p = [30, 35, 15, 5, 10, 20, 25] # CLRS example ob pg. 376
verbose = True

(m, s) = matrix_chain_order(p, verbose)
