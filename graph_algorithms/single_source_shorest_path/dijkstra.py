from Graph import Vertex
from Graph import Edge
from Graph import Graph
from heapsort import Heap
from heapsort import swap

def main():
    n = 5
    G = Graph(n=n)

    G.insert(0,1,3)
    G.insert(0,3,5)
    G.insert(1,2,6)
    G.insert(1,3,2)
    G.insert(2,4,2)
    G.insert(3,1,1)
    G.insert(3,2,4)
    G.insert(3,4,6)
    G.insert(4,0,3)
    G.insert(4,2,7)

    print("*** Graph ***")
    G.print(True)

    # Initialize starting vertex
    for v in G.V:
        v.d *= -1
    G.V[0].d = 0

    # Organize vertices into a min heap
    H = Heap(array=G.V)
    H.build_max_heap() # NOTE: modified max heap
    print("*** Min Heap ***")
    H.print()

    # Now perform Dijkstra's algorithm
    while not H.is_empty():
        vertex = H.heap_extract_max()

        H.print()
        print()

        #print(u.index, u.distance)
        for edge in G.adj[vertex.index]:
            v = G.V[edge.v] # get vertex object

            vertex.d *= -1
            v.d *= -1

            # "Relax" upper bound, remember our weird "negative" max heap setup
            if v.d > vertex.d + edge.weight:
                v.d = vertex.d + edge.weight
                v.pred = vertex

            vertex.d *= -1
            v.d *= -1
    
    # Print results
    print("Vertex\tDist.\tPred.")
    for vertex in G.V:
        if vertex.pred is None:
            tmp = '/'
        else:
            tmp = vertex.pred.index
        print(f"{vertex.index}\t{vertex.d*-1}\t{tmp}")

if __name__ == "__main__":
    main()
