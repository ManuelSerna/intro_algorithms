def partition(A:list, left:int, right:int) -> int:
    """Custom quicksort partition for Vertex objects."""
    pivot = A[right].weight # we will compare weights later
    i = left - 1

    for j in range(left, right):
        if A[j].weight <= pivot: # compare weights
            # swap objects
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

    i += 1
    tmp = A[i] # sorted value
    A[i] = A[right]
    A[right] = tmp

    return i

def quicksort_helper(A:list, left:int, right:int):
    if left < right:
        mid = partition(A, left, right)
        quicksort_helper(A, mid+1, right)
        quicksort_helper(A, left, mid-1)

def quicksort(A:list):
    left = 0
    right = len(A)-1
    quicksort_helper(A, left, right)

class Vertex():
    def __init__(self, index:int, set_addr=None):
        self.index = index
        self.set_addr = set_addr # refernce to Graph instance
        
        self.discover_time = None
        self.finish_time = None
        
        self.color = 'white' # {white, gray, black}

        # For checking membership in the same class (arbitray class)
        self.set = None # this will be the reference an arbitrary class

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

class Set():
    def __init__(self):
        """Set class for Kruskal algorithm.

        The set 'members' is a simple list.
        This class can check object membership (check if the object reference 
        is already in the list).
        This class can insert any object (into 'members').
        """
        self.members = [] # a list of object references

    def check_membership(self, v):
        return v in self.members

    def insert(self, v):
        if self.check_membership(v):
            raise Exception("f[Set class] (Re-)Inserting Vertex {v} into members list {self.members}.")
        v.set = self
        self.members.append(v)

def set_union(set1:Set, set2:Set) -> Set:
    """Union for objects of the custom 'Set' class.

    For simplicity, this function just grabs each set's 'members'
    attribute list and copies them over to a new Set object.
    Keep in mind that Set.insert() will update the objects' 'set'
    attribute will be updated to reference this new Set instance.

    Object references will be copied from arg set1 first, then set2.
    """
    new_set = Set() # empty set

    for i in range(len(set1.members)):
        new_set.insert(set1.members[i])

    for j in range(len(set2.members)):
        new_set.insert(set2.members[j])

    return new_set

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

def kruskal(G:Graph, s:Vertex) -> Set:
    mst = Set() # empty set for minimum spanning tree

    # Every vertex/node is in its own set
    for v in G.V:
        s = Set()
        s.insert(v)

    # Sort edges in G.E by nondecreasing weight
    quicksort(G.E)
    
    # Iterate through the smallest edges first, and grow the final set
    for edge in G.E:
        if G.V[edge.u].set != G.V[edge.v].set:
            mst.insert(edge)
            set_union(G.V[edge.u].set, G.V[edge.v].set)

    return mst

def main():
    # Create graph
    n = 8
    G = Graph(n=n, is_directional=False)

    # Insert edges
    G.insert(0,1,2.0)
    G.insert(0,2,3.0)
    G.insert(0,3,4.0)
    G.insert(1,6,2.0)
    G.insert(2,3,5.0)
    G.insert(2,4,1.0)
    G.insert(2,5,3.0)
    G.insert(2,6,4.0)
    G.insert(3,4,3.0)
    G.insert(3,7,4.0)
    G.insert(4,7,1.0)
    G.insert(4,5,2.0)

    G.print(False)

    s = G.V[0]

    # Run Kruskal
    mst = kruskal(G, s)

    # Check
    for edge in mst.members:
        print(edge.print(True))



if __name__ == "__main__":
    main()
