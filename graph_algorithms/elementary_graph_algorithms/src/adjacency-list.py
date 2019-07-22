#************************************************
'''
    Adjacency-list representation of a graph.

    This file includes a node definition for some node u and a adjacency list representation of a graph.

    The node class contains attributes:
     v: the vertex u is connected to that makes edge (u, v).
     w: weight of edge (u, v). For undirected graphs, it will be 1 by default.

    The adjacency class contains attributes:
     n: the number of nodes the list adj contains
     is_directed: Boolean flag to dictate whether the graph is directed or not
     adj: array/list to store vertices
'''
#************************************************

class Node():
	def __init__(self, vertex, weight=1):
		self.v = vertex
		self.w = weight

	def get_node(self):
		return (self.v, self.w)

class AdjacencyList():
    def __init__(self, n, is_directed=False):
        self.n = n
        self.is_directed = is_directed
        self.adj = []
        for i in range(n):
            self.adj.append([])

    # Print the adjancency list with the option to show weights.
    def print(self, show_w=False):
        for u in range(self.n):
        	edges = self.adj[u] # edges u is connected to
        	paths = str(u) # string that will printed, shows what paths u makes
        	for i in range(len(edges)):
        		v = self.adj[u][i]
        		if show_w:
        			paths += '->{}(w={})'.format(v.v, v.w)
        		else:
        			paths += '->{}'.format(v.v)
        	print(paths) # print all edges (u, v) for current u

    # Insert edge (u, v) with weight (if directed).
    def insert(self, u, v, w=1):
    	self.adj[u].append(Node(v, w))
    
    # Remove edge (u, v) from graph.
    # Look at index u, look at all v nodes that make edges (u, v).
    def remove(self, u, v):
    	edges = self.adj[u]
    	for i in range(len(edges)):
    		if self.adj[u][i].v == v:
    			print('found it at index {}! {}'.format(i, self.adj[u][i].v))
    			del self.adj[u][i]
    			break
