#************************************************
# Rod cutting (bad implementation)
#************************************************

def max(a, b):
    if a > b:
        return a
    else:
        return b

def cut_rod(p, n):
    print("cutting, ", n)
    if n == 0:
        return 0
    q = -999
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod(p, n-i))
    return q


# Begin cutting rod
prices = [1, 4, 2, 3]#, 4, 5, 3, 2, 0] # price array for length i
length = 4 # rod length
print("max profit: ", cut_rod(prices, length))