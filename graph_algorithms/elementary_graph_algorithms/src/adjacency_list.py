#************************************************
# Adjacency-list representation of a graph.
#************************************************

# Sentinel for infinity
infty = 999999

#================================================
'''
    The vertex class contains attributes:
        color: color of vertex in the graph, these are treated as single characters, it is white by default. Possible values:
            - w: white--vertex not discovered yet.
            - g: grey--vertex discovered, but may still be connected to undiscovered (w) vertices.
            - b: black--nothing left to discover, we are done with the current vertex.
        d: discovery time for the vertex. Will be assigned when vertex is made grey, assigned sentinel value of infinity. Will be an integer.
        f: finish time. Will be assigned when vertex is assigned color black, null by default.

    * To access these vertices, create a list V, and that will denote which vertex is which. How many vertices there are and thus how long V is will be determined by the variable `n` in the adjlist class constructor.
'''
#================================================
class vertex():
    def __init__(self, color='w', f=None, v=None, pred=None):
        self.color = color
        self.d = infty
        self.f = f
        self.pred = pred



#================================================
'''
    The edge class contains attributes:
        u: start vertex of edge (u, v).
        v: end vertex of edge (u, v).
        w: weight of edge, 1 by default.

    * In the adjlist class, the list adj will be created and will house these objects in it.
'''
#================================================
class edge():
    def __init__(self, u, v, w=1):
        self.u = u
        self.v = v
        self.w = w

    def get(self, show_w=False):
        if show_w:
            return "({}, {}, w={})".format(self.v, self.u, self.w)
        else:
            return "({}, {})".format(self.v, self.u)



#================================================
'''
    The adjacency class contains attributes:
        n: the number of vertices the list adj contains. If not set, the graph will have one vertex.
        is_directed: Boolean flag to dictate whether the graph is directed or not. The graph is undirected by default.
        adj: list of edges any vertex i makes.
'''
#================================================
class adjlist():
    def __init__(self, n=1, is_directed=False):
        self.n = n
        self.is_directed = is_directed
        
        # Crate set of vertices V
        self.V = []
        for i in range(n):
            self.V.append(vertex())

        # Create list of edges adj for each vertex i
        self.adj = []
        for i in range(n):
            self.adj.append([])

    # Print the adjancency list with the option to show weights.
    def print(self, show_w=False):
        print("Printing adjacency list.")
        for i in range(self.n):
            edges = self.adj[i]
            paths = str(i)
            for j in range(len(edges)):
                paths += "->{}".format(edges[j].get(show_w))
            print(paths)

    # Insert edge (u, v) with weight (if directed) into adj.
    def insert(self, u, v, w=1):
        self.adj[u].append(edge(u, v))

    # Remove edge (u, v) from graph.
    # Look at index u, look at all vertices that make edges (u, v).
    def remove(self, u, v):
    	edges = self.adj[u]
    	for i in range(len(edges)):
    		if self.adj[u][i].v == v:
    			print('Found at index {}! {}'.format(i, self.adj[u][i].get(False)))
    			del self.adj[u][i]
    			break
