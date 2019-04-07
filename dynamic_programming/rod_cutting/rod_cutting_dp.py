#************************************************
# Dynamic Programming- rod cutting problem. 
# Note: top-down approach not implemented since it's bad.
#************************************************

def max(a, b):
    if a > b:
        return a
    else:
        return b

#------------------------------------------------
# Extended bottom-up approach implementation
#------------------------------------------------

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
            q = max(q, p[i] + r[j-i])
        r[j] = q # solved subproblem of size j (rod of size j)
    return r[n]
    
#------------------------------------------------
# Computes, for each rod size j, not only the maximum revenue r[j], but also s[j], the optimal size of the first piece to cut off
#------------------------------------------------
def extended_bottom_up_cut_rod(p, n):
    # Let r[0..n] and s[0..n] be new arrays
    r = [0 for i in range(n+1)]
    s = [0 for i in range(n+1)]

    r[0] = 0

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
# MAIN
# Note: for methods to properly work, subtract value 1 from your list lengths.
#================================================
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
length = len(prices) - 1

print("Rod length: ", length)
print("Given the following prices for smaller unit lengths.")
print(prices)
print()

# Bottom-up calls
# (1)
#print("Best price: ", bottom_up_cut_rod(prices, length))

# (2)
print_cut_rod_solution(prices, length)
