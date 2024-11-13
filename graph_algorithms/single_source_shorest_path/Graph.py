class Vertex():
    def __init__(self, index:int, distance:int=99999):
        self.index = index
        self.d = distance
        self.pred = None
        #self.discover_time = None
        #self.finish_time = None
        #self.color = 'white' # {white, gray, black}

class Edge():
    def __init__(self, u:Vertex=None, v:Vertex=None, weight=1.0):
        self.u = u
        self.v = v
        self.weight = weight

    def print(self, show_w:bool):
        if show_w:
            return f"(u={self.u}, v={self.v}, weight={self.weight})"
        else:
            return f"{self.v}"

class Graph():
    def __init__(self, n:int=1, is_directional=True):
        """Adjacency List graph class."""
        self.n = n
        self.is_directional = is_directional

        # Vertices V
        self.V = []
        for i in range(n):
            self.V.append(Vertex(index=i))

        # Edges E
        self.E = []

        # Adjacency List: list of edges
        self.adj = []
        for i in range(n):
            self.adj.append([])

    def print(self, show_w:bool):
        for i in range(self.n):
            edges = self.adj[i]
            paths = str(i)
            for j in range(len(edges)):
                paths += f"->{edges[j].print(show_w)}"
            print(paths)
        print()

    def insert(self, u:int, v:int, weight):
        """Insert edge by indexing the vertices u and v and providing weight."""
        edge = Edge(u, v, weight)
        self.E.append(edge)
        self.adj[u].append(edge)

        if not self.is_directional:
            # If undirected, then insert 
            reverse_edge = Edge(v, u, weight)
            self.E.append(reverse_edge)
            self.adj[v].append(reverse_edge)
