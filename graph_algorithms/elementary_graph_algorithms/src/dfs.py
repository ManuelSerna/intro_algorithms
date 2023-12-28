"""Depth-first search.

Demo on the graph from the CLRS book, DFS section.

Original graph:
Y<---Z<---S    M
|   ^|  / ^  /^|
|  / | /  | / ||
v /  vv   |v  |v
X<---W<---V<---U

Adapted:
0<---1<---2    3
|   ^|  / ^  /^|
|  / | /  | / ||
v /  vv   |v  |v
4<---5<---6<---7
"""

from AdjacencyList import AdjacencyList

# Global variables
time = 0 # for discovery & finish times
finished = [] # insert vertices here as they finish

def dfs_visit(G=None, s=None):
    """ Depth-first search starting from a single node.

    Args:
        G: AdjacencyList object to represent the graph
        s: Vertex object that is our starting vertex
    """
    # Global vars
    global time
    global finished

    time += 1
    s.d = time
    s.color = 'g' # signal that vertex is discovered

    for i in G.adj[s.index]:
        # Get vertex
        vertex = G.V[i.v]

        if vertex.color == 'w':
            # Explore from newly-discovered vertex
            vertex.pred = s
            dfs_visit(G, vertex)

    time += 1
    s.f = time
    s.color = 'b'

    # Global updates
    finished.append(s)

def dfs(G=None):
    """Depth-first search with no starting node.

    I.e., we go through *all* nodes in graph G in order of number index,
    and for each vertex, connected vertices are visited by the order in 
    which they were inserted (what is first in a vertice's adjacency list).

    Args:
        G: AdjacencyList object to represent the graph
    """
    # Iterate and explore from all unvisited/'w' nodes
    for u in G.V:
        if u.color == 'w':
            dfs_visit(G, u)

def main():
    # Initialize graph with n nodes/vertices
    n = 8
    G = AdjacencyList(n)

    # Insert edges
    G.insert(0,4)
    G.insert(1,0)
    G.insert(1,5)
    G.insert(2,1)
    G.insert(2,5)
    G.insert(3,6)
    G.insert(3,7)
    G.insert(4,1)
    G.insert(5,4)
    G.insert(6,2)
    G.insert(6,5)
    G.insert(7,3)
    G.insert(7,6)

    G.print()

    # Perform DFS
    dfs(G)

    # Check work on DFS
    """
    If we're using the graph above,
    then we get the below output:

    0->4
    1->0->5
    2->1->5
    3->6->7
    4->1
    5->4
    6->2->5
    7->3->6

    Updated G.V
    *************************
    * Index: 0
    ...Color: b
    ...Discovery Time: 1
    ...Finish Time: 8
    ...Pred: None

    * Index: 1
    ...Color: b
    ...Discovery Time: 3
    ...Finish Time: 6
    ...Pred: 4

    * Index: 2
    ...Color: b
    ...Discovery Time: 9
    ...Finish Time: 10
    ...Pred: None

    * Index: 3
    ...Color: b
    ...Discovery Time: 11
    ...Finish Time: 16
    ...Pred: None

    * Index: 4
    ...Color: b
    ...Discovery Time: 2
    ...Finish Time: 7
    ...Pred: 0

    * Index: 5
    ...Color: b
    ...Discovery Time: 4
    ...Finish Time: 5
    ...Pred: 1

    * Index: 6
    ...Color: b
    ...Discovery Time: 12
    ...Finish Time: 13
    ...Pred: 3

    * Index: 7
    ...Color: b
    ...Discovery Time: 14
    ...Finish Time: 15
    ...Pred: 3
    """
    print("\n\nUpdated G.V\n*************************")
    for i in G.V:
        i.get_info()

    # Topological sort
    """
    With DFS complete, we have topological sort
     based on the general DFS starting from vertex indexed 0.
    Remember there are many possiblities for DFS and therefore
     topological sort, which depend on the following.

    1) how we traverse G.V (our list of vertices)
    2) how we traverse the adjacency list G.adj
    """
    print("\n\nCorresponding topological Sort\n*************************")
    for i in finished:
        i.get_info()

if __name__ == "__main__":
    main()

