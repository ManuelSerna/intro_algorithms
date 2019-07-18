#************************************************
'''
    Activity Selection Problem.
    
    Each activity has a start time s and a finish time f such that 0 <= s < f < infty.
    Activities 1 and 2 are compatible with each other if:
        [s1, f1) and [s2, f2) do not overlap.
    
    In the activity selection problem, we want to find the max number of mutually compatible activities.
    
    In the example given in CLRS, take the following set S of activity times
    (include ficticious activity 0)
    
    i    |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11
    -----+--+--+--+--+--+--+--+--+--+--+--+--
    s(i) |0 |1 |3 |0 |5 |3 |5 |6 |8 |8 |2 |12
    f(i) |0 |4 |5 |6 |7 |9 |9 |10|11|12|14|16 <-- notice finish times are sorted, this is an assumption.
'''
#************************************************

import time as t

# Greedy solution
def greedy_activity_selector(s, f):
    n = len(s)
    A = [1] # add activity 1 since it starts first
    k = 1   # index most recent addition to A
    for m in range(2, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A
    
#================================================
# Test greedy implementation
#================================================
# Set of starting times s, finish times f for activities a
s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

run_time = 0
run_time = (t.time() * 1000.0)
a = greedy_activity_selector(s, f)
run_time = (t.time() * 1000.0) - run_time

print('time: {} ms'.format(run_time))
print('optimal sequence of activities:\n{}'.format(a))
