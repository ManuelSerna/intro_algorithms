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

from AdjacencyList import AdjacencyList

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
            self.Q = self.Q + [None]

    def is_full(self):
        if self.head == self.tail and self.Q[self.tail] != None:
            return True
        else:
            return False
    
    def is_empty(self):
        if self.Q[self.head] == None:
            return True
        else:
            return False
    
    def enqueue(self, x):
        if self.is_full():
            raise Exception("overflow!")
        else:
            self.Q[self.tail] = x
            if self.tail == self.length-1:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("underflow!")
        else:
            x = self.Q[self.head]
            self.Q[self.head] = None
            if self.head == self.length-1:
                self.head = 0
            else:
                self.head += 1
            return x
    
    def print(self):
        print(self.Q)



#------------------------------------------------
'''
    Breadth-first search.
    Parameters:
        G: graph with vertices and adjacency list.
        s: starting vertex (vertex object)
'''
#------------------------------------------------
def bfs(G, start):
    # Get vertex from G.V at index "start"
    s = G.V[start]
    
    # Vertex values already assigned, no need to initialize each vertex
    
    s.color = 'g'
    s.d = 0
    # s.pred is already NIL (look in vertex class constructor)
    
    # Create empty queue
    Q = Queue(G.n)
    
    # Keep exploring each vertex's adjacency list to look for gray vertices.
    Q.enqueue(s)
    
    # Keep dequeuing vertices and see, in the adj array, which other vertices they are connected to, we refer to each vertice's attributes in the V list.
    while not Q.is_empty():
        u = Q.dequeue()
        
        # Loop through vertices connected to u to make edges (u, v); we get the v values from the edges list G.adj, and then look at G.V.
        for i in G.adj[u.index]:
            # Get vertex
            v = G.V[i.v]
            v.get_info()
            
            # Check color
            if v.color == 'w':
                v.color = 'g'
                v.d = u.d + 1
                v.pred = u
                Q.enqueue(v)
            
        u.color = 'b'



#------------------------------------------------
# Create graph G with n nodes
#------------------------------------------------
n = 8
G = AdjacencyList(n)
G.insert(0, 1) # insert: (start node u, end node v)
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

# Output sample graph
G.print()

# Begin breadth-first search starting at vertex with label 1 (look at ascii figure)
s = 1
bfs(G, s)

print("\n\nUpdated G.V\n************************")
for i in G.V:
    i.get_info()
