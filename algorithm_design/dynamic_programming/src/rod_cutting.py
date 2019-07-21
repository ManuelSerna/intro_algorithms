#************************************************
# Dynamic Programming Example - rod cutting.
#************************************************

import time as t

def max(a, b):
    if a >= b:
        return a
    else:
        return b

#================================================
# Recursive (inefficient) version.
#================================================
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod(p, n-i))
    return q

#================================================
# Dynamic Programming methods
# Computes, for each rod size j, not only the maximum revenue r[j], 
#     but also s[j], the optimal size of the first piece to cut off.
#================================================

# Regular bottom-up, returns only max profit
def bottom_up_cut_rod(p, n):
    # Let r[0..n] be a new array, go up to n+1 to save r[n]--optimal solution
    r = [None for i in range(n+1)]
    r[0] = 0 # no length = zero profit
    
    '''
    for i in range(n+1):
        print(r[i])
    '''
    # Get values for smaller cuts starting at length = 1 up to n
    for j in range(1, n+1):
        q = -1 # set up max value holder
        # At sub length j, start from 1 and go up to length j, these are just the lengths that add up to j (including j + 0), and then see what combinations of prices of given lengths will give the best profit, keep storing this in q
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q # solved subproblem of size j (rod of size j)
    return r[n]
    
#------------------------------------------------
# Extended version of bottom-up
# Computes, for each rod size j, not only the maximum revenue r[j], but also s[j], the optimal size of the first piece to cut off
#------------------------------------------------
def extended_bottom_up_cut_rod(p, n):
    # Let r[0..n] and s[0..n] be new arrays
    r = [0 for i in range(n+1)]
    s = [0 for i in range(n+1)]

    r[0] = 0

    # Start at 0, then take each possible profit sum combination from 1..i and i+1..j, record the max price as you go up to j.
    # The index that gives this max profit is then stored.
    for j in range(n+1):
        q = -1
        for i in range(j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return (r[n], s)

def print_cut_rod_solution(p, n):
    (max_price, s) = extended_bottom_up_cut_rod(p, n)
    
    # Print optimal cuts
    print("Optimal cut positions:")
    while n > 0:
        print(s[n])
        n = n - s[n]
    
    print("Max profit: ", max_price)


#================================================
# Test rod cutting with different approaches.
#================================================
#prices = [1, 4, 2, 3]#, 4, 5, 3, 2, 0]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
length = len(prices)
run_time = 0

print("Rod length: ", length)
print("Given the following prices for smaller unit lengths.")
print(prices)
print()

# Test 1
print('Testing recursive version.')
run_time = (t.time() * 1000.0)
print("max profit: ", cut_rod(prices, length))
run_time = (t.time() * 1000.0) - run_time
print('time: {} ms'.format(run_time))
print()

# Test 2
print('Testing dp version (bottom-up).')
run_time = (t.time() * 1000.0)
print("Best price: ", bottom_up_cut_rod(prices, length))
run_time = (t.time() * 1000.0) - run_time
print('time: {} ms'.format(run_time))
print()

