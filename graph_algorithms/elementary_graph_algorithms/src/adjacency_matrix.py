#************************************************
# Adjacency-matrix representation of a graph.
#************************************************

class adjmatrix():
    # Create |V| x |V| (n x n) matrix adj
    def __init__(self, n):
        self.n = n
        self.adj = []
        for i in range(self.n):
            row = []
            for j in range(n):
                row.append(0)
            self.adj.append(row)

    def print_adj(self):
        for i in range(self.n):
            print(self.adj[i])

    # Connect vertices u and v to make edge (u, v) with weight w (1 default)
    def insert(self, u, v, w=1):
        self.adj[u][v] = w
        print('Inserted edge ({}, {}).'.format(u, v))

    # Remove edge (u, v)
    def remove(self, u, v):
        self.adj[u][v] = 0
        print('Removed edge ({}, {}).'.format(u, v))
