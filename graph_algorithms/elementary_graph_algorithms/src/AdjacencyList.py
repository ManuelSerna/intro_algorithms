#************************************************
# Adjacency-list representation of a graph.
#************************************************

# Sentinel for infinity
infty = 999999

#================================================
'''
    The vertex class contains attributes:
        index: the number label for each vertex in the graph, these will be integers.
    
        color: color of vertex in the graph, these are treated as single characters, it is white by default. Possible values:
            - w: white--vertex not discovered yet.
            - g: grey--vertex discovered, but may still be connected to undiscovered (w) vertices.
            - b: black--nothing left to discover, we are done with the current vertex.
        
        d: discovery time for the vertex. Will be assigned when vertex is made grey, assigned sentinel value of infinity. Will be an integer.
        
        f: finish time. Will be assigned when vertex is assigned color black, null by default.

        pred: a Vertex object that serves as the predecessor to the current vertex

    * To access these vertices, create a list V, and that will denote which vertex is which. How many vertices there are and thus how long V is will be determined by the variable `n` in the adjlist class constructor.
'''
#================================================
class Vertex():
    def __init__(self, index:int=-1, color:str='w', f:int=None, v=None, pred=None):
        self.index:int = index
        self.color:str = color
        self.d:int = infty
        self.f:int = f
        self.pred = pred
    
    def get_info(self):
        """Get vertex info."""
        label = "* Index: {}\n...Color: {}\n...Discovery Time: {}\n...Finish Time: {}\n...Pred: {}\n"

        if self.pred is not None:
            label = label.format(self.index, self.color, self.d, self.f, self.pred.index)
        else:
            label = label.format(self.index, self.color, self.d, self.f, self.pred)

        print(label)



#================================================
'''
    The edge class contains attributes:
        u: start vertex of edge (u, v), integer.
        v: end vertex of edge (u, v), integer.
        w: weight of edge, 1 by default, integer.

    * In the adjlist class, the list adj will be created and will house these objects in it.
'''
#================================================
class Edge():
    def __init__(self, u:Vertex=None, v:Vertex=None, w:int=1):
        self.u:Vertex = u
        self.v:Vertex = v
        self.w:int = w

    def get_info(self, show_w=False):
        """Print edge info."""
        if show_w:
            return "({}, {}, w={})".format(self.v, self.u, self.w)
        else:
            return "{}".format(self.v) # only return end edge



#================================================
'''
    The adjacency class contains attributes:
        n: the number of vertices the list adj contains. If not set, the graph will have one vertex.
        is_directed: Boolean flag to dictate whether the graph is directed or not. The graph is undirected by default.
        adj: list of edges any vertex i makes.
'''
#================================================
class AdjacencyList():
    def __init__(self, n:int=1, is_directed:bool=False):
        self.n = n
        self.is_directed = is_directed
        
        # Crate set of vertices V
        self.V = []
        for i in range(n):
            self.V.append(Vertex(index=i))

        # Create list of edges adj for each vertex i
        self.adj = []
        for i in range(n):
            self.adj.append([])

    def print(self, show_w=False):
        """Print graph info.

        Args:
            show_w: (bool) print edge weights (e.g., if graph has weighted edges, 
                or don't show if graph is unweighted). Default is False.
        """
        print("Printing adjacency list.")
        for i in range(self.n):
            edges = self.adj[i]
            paths = str(i)
            for j in range(len(edges)):
                paths += "->{}".format(edges[j].get_info(show_w))
            print(paths)
        print()

    def insert(self, u, v, w=1):
        """Insert edge.

        Args:
            u: (int) index for start vertex
            v: (int) index for end vertex
            w: (int) weight for edge (default=1 for "unweighted")
        """
        self.adj[u].append(Edge(u, v))

    def remove(self, u, v):
        """ Remove edge (u,v) from the graph.

        Args:
            u: (int) index for start vertex
            v: (int) index for end vertex
        """
        edges = self.adj[u]
        for i in range(len(edges)):
            if self.adj[u][i].v == v:
                print('Found at index {}! {}'.format(i, self.adj[u][i].get_info(False)))
                del self.adj[u][i]
                break
