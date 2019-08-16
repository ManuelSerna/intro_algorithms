#************************************************
'''
    Breadth-first search.
    Demo on graph--figure 22.3--from CLRS from page 22.

    Original graph:
    r--s  t--u
    |  | /| /|
    v  w--x--y

    Adapted:
    0--1  2--3
    |  | /| /|
    4  5--6--7
'''
#************************************************

import adjacency_list as adj

#------------------------------------------------
# Include queue class from elementary graphs section.
#------------------------------------------------
class Queue():
    def __init__(self, length):
        self.length = length
        self.head = 0
        self.tail = 0
        self.Q = []
        for i in range(length):
            self.Q = self.Q + [-1]

    def enqueue(self, x):
        self.Q[self.tail] = x
        if self.tail == self.length:
            self.tail = 1
        else:
            self.tail += 1

    def dequeue(self):
        x = self.Q[self.head]
        self.Q[self.head] = -1
        if self.head == self.length:
            self.head = 1
        else:
            self.head += 1
        return x



#------------------------------------------------
'''
    Breadth-first search.
    Parameters:
        G: graph with vertices and adjacency list.
        s: starting vertex.
'''
#------------------------------------------------
def bfs(G, s):
    # Vertex values already assigned
    s.color = 'g'
    s.d = 0
    #TODO: continue




#------------------------------------------------
# Create graph G with n nodes
#------------------------------------------------
n = 8
G = adj.adjlist(n)
G.insert(0, 1)
G.insert(0, 4)
G.insert(1, 0)
G.insert(1, 5)
G.insert(2, 3)
G.insert(2, 5)
G.insert(2, 6)
G.insert(3, 2)
G.insert(3, 6)
G.insert(3, 7)
G.insert(4, 0)
G.insert(5, 1)
G.insert(5, 2)
G.insert(5, 6)
G.insert(6, 2)
G.insert(6, 3)
G.insert(6, 5)
G.insert(6, 7)
G.insert(7, 3)
G.insert(7, 6)

#G.print(False)
bfs(G, G.V[1])
