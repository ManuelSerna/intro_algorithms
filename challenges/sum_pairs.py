""" 
"""

def num_sum_pairs(A:list, m:int):
    """ Get number of sum pairs that add up to m."""
    # Make count array, linear-time processing
    max_val = max(A) # linear time w.r.t. length of A
    counts = [0 for i in range(max_val+1)] # linear time w.r.t. unique elements in A
    
    for i in range(len(A)): # linear time w.r.t. length of A
        counts[A[i]] += 1

    # Now, 'counts' has counts of each element, which we can use to 
    # get pairs quickly given arg. m
    pairs = 0

    for i in range(len(counts)):
        if counts[i] > 0:
            # We only care about non-zero sum operand,
            # notice we do not avoid cases where 0 + diff = m; m, diff > 0
            diff = m - i

            if diff == 0:
                # Case: one operand is zero, just add number of instances
                pairs += counts[i]
            else:
                pairs += counts[i] * counts[diff]
                counts[diff] = 0 # do not count twice
                #import pdb;pdb.set_trace()

    return pairs

def main():
    #A = [3,3,3,4,4]
    A = [1,3,2,4,6,3,3,7,4]
    m = 7
    pairs = num_sum_pairs(A, m)
    
    print("A:\n", A)
    print("Number of pairs: ", pairs)

if __name__ == "__main__":
    main()
