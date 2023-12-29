""" Transpose Example and Demo

Example is below.
Graph G:
0--->1    2
|   ^|  / |
|  / | /  |
v /  vv   v
3<---4    5<-(loop)


...and transposed G:
0<---1    2
^  / ^   ^^
| /  |  / |
|v   | /  |
3--->4    5<-(loop)


The transpose operation takes

O(|V|^2)-time

since, worst-case scenario, all vertices may pair with all other vertices.
"""
from AdjacencyList import AdjacencyList as Graph

def transpose(G:Graph=None) -> Graph:
    Gt = Graph(n=G.n)

    for u in G.V:
        for edge in G.adj[u.index]:
            v = edge.v # get end vertex v in (u,v)
            Gt.insert(v, u.index) # insert reverse-direction edge (v,u)

    return Gt

def main():
    n = 6
    G = Graph(n=n)

    # Insert
    G.insert(0,1)
    G.insert(0,3)
    G.insert(1,4)
    G.insert(2,4)
    G.insert(2,5)
    G.insert(3,1)
    G.insert(4,3)
    G.insert(5,5)
    
    # Transpose
    print('Original:')
    G.print()
    
    Gt = transpose(G)

    print('Transposed:')
    Gt.print()

    #print("\n\nUpdated G.V\n*******************************")
    #for i in G.V:
    #    i.get_info()

if __name__ == "__main__":
    main()
