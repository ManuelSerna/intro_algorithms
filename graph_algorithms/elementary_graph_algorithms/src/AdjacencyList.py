# 'Sentinel' value for infinity
infty = 999999



class Vertex():
    def __init__(self, index:int=-1, color:str='w', f:int=None, v=None, pred=None):
        """ Vertex class

        Args:
            index: (int) label for each vertex in the graph
            color: (str) color of vertex in the graph
                Possible values:
                 w: white--vertex not discovered yet.
                 g: grey--vertex discovered, but may still be connected to undiscovered (w) vertices.
                 b: black--nothing left to discover, we are done with the current vertex.

                 NOTE: I am too lazy to make a setter and redo all my code again...
            
            d: (number) discovery time for the vertex; this is set when we discover this vertex for the first time
            f: (number) finish time; this is set when we no longer have any new vertices to discover
                with this vertex in the path.
            pred: (Vertex) a Vertex object that serves as the predecessor to the current vertex
        """
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



class Edge():
    def __init__(self, u:Vertex=None, v:Vertex=None, w:int=1):
        '''Edge class
            The edge class contains attributes:
                u: start vertex of edge (u, v), integer.
                v: end vertex of edge (u, v), integer.
                w: weight of edge, 1 by default, integer.
        '''
        self.u:Vertex = u
        self.v:Vertex = v
        self.w:int = w

    def get_info(self, show_w=False):
        """Print edge info.
        
        Args:
            show_complete: (bool) if True, then show edge (u,v) and weight,
                else show only end vertex v
        """
        if show_w:
            return f"(u={self.u}, v={self.v}, w={self.w})"
        else:
            return f"{self.v}"



class AdjacencyList():
    def __init__(self, n:int=1, is_directed:bool=False):
        """ Adjacency List class

        Represent a graph with vertices/nodes with its edges represented in a list of Edge objects.

        Args:
            n: (int) the number of vertices the list adj will contain. 
                If not set, the graph will have one vertex.
            is_directed: (bool) flag to dictate whether the graph is directed or not.
        
        NOTES:
        I)
        The attribute V is a list of Vertex objects.
        Note, then, that each Vertex object's 'index' attribute does not necessarily indicate
        their position in V.

        II)
        The attribute "adj" is a list of of lists of Edge objects.
        To access data in adj, there are several cases to consider.
        Given AdjacencList object instance called G:

            (1) with Vertex object reference s:
            
                G.adj[s.index]

            will return a list of edges with s as the starting vertex,
            i.e., we get edges in the form (s, v), where v is some other Vertex reference.

            (2) with integer i
            
                G.adj[i]

            returns a list of vertices with whatever vertex is indexed by i in 'adj' 
             as the starting vertex.
        """
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
        """Insert edge (u,v).

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
