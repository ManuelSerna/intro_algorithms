# intro_algorithms

This is a collection of my notes and code for various algorithms, data structures, and the like. If anyone finds this, feel free to look at what I have and perhaps also add improvements. Also, I would recommend others read the book with these notes so as to make sense of what the authors were trying to convey.

## Notes before reading any notes
  * Whenever I use ```log n```, I mean the common logarithm (log base 10).

## Sorting algorithms and data structures covered:
Planned Structure

    * Analysis: "analysis". Purpose: mathematics with algorithms
        |-> chapter 2 content --DONE
        |-> chapter 3 content
    
    * Algorithm Design: "algorithm_design"
        |-> chapter 4 content
        |-> dynamic programming
        |-> greedy algorithms
    
    * Sorting Algorithms: "sorting_algorithms"
        |-> insertion sort (code only) --DONE
        |-> merge sort (code only) --DONE
        |-> quicksort
        |-> counting sort
        |-> radix sort
        |-> bucket sort
	(heap sort will be included in the heaps data structure topic)

    * Data Structures: "data_structures"
        |-> elementary data structures
            |-> stacks
            |-> queues
            |-> linked lists
        |-> hash tables
        |-> binary search trees
        |-> red-black trees
        |-> augmenting data structures
    
    * Graph Algorithms: "graph_algorithms"
        |-> elementary graph algorithms
            |-> representations of graphs
            |-> breadth-first search
            |-> depth-first search
            |-> topological sort
            |-> strongly connected components
        |-> minimum spanning trees
            |-> kruskal
            |-> prim
        |-> single-source shortest paths
            |-> bellman-ford
            |-> dijkstra
        |-> all-pairs shortest paths
            |-> floyd-warshall
            |-> johnson
    
    Content
    ---------------------------------------------
    * Chapter 2: getting started
        - insertion sort (latex)
        - analyzing and designing algorithms (latex)

    * Chapter 3: growth of functions
        - asymptotic notation (latex)
        - standard notations and common functions (latex)

    * Chapter 4: Recurrences (need to create .tex notes for the last 3 sections)
        - maximum subarray problem 
        - strassen's algorithm for matrix multiplication 
        - substitution method
        - recursion tree method
        - master method
    
    * Chapter 6: Heapsort (need to create .tex notes for all sections, and implement)
        - heaps
        - maintaining the heap property
        - building a heap
        - heapsort algorithm
        - priority queues
    
    * Chapter 7: Quicksort (need to create .tex notes for both sections)
        - description of quicksort
        - performance of quicksort
    
    * Chapter 8: Sorting in Linear Time (need to create .tex notes for all sections)
        - lower bounds for sorting (need to create .tex notes)
        - counting sort
        - radix sort
        - bucket sort
    
    * Chapter 11: Hash tables (need to create .tex notes)
        - direct-address table
        - hash tables
        - hash functions
        - open addressing
    
    * Chapter 12: Binary Search Trees--review (need to create .tex notes)
        - what is a binary search tree?
        - querying a binary search tree
        - insertion and deletion
    
    * Chapter 13: Red-Black Trees (need to create .tex notes)
        - properties
        - rotations
        - insertion
        - deletion
    
    * Chapter 15: Dynamic Programming (need to create .tex notes)
        - rod cutting problem
        - matrix-chain multiplication
        - elements of dynamic programming
        - longest common subsequence
        - optimal binary search trees
    
    * Chapter 16: Greedy Algorithms (need to create .tex notes)
        - activity selection problem
        - elements of greedy strategy
        - huffman codes
    
    * Chapter 22: Elementary Graph Algorithms (need to create .tex notes)
        - representations of graphs
        - BFS
        - DFS
        - topological sort
        - strongly-connected components
    
    * Chapter 23: Minimum Spanning Trees (need to create .tex notes)
        - growing a min span tree
        - Kruskal
        - Prim
    
    * Chapter 24: Single-Source Shortest Paths (need to create .tex notes)
        - bellman-ford algorithm
        - single-source shortest paths in directed acyclic graphs
        - dijkstra's algorithm
    
    * Chapter 25: All-Pairs Shortest Paths (need to create .tex notes)
        - floyd-warshall algorithm
        - johnson's algorithm for sparse graphs

    I will add other topics/chapters I find interesting to this in the future.
    My plan is to finish the chapters specified above by August for sure.

## Resources
Overleaf's documentation on LaTeX.
https://www.overleaf.com/learn


## References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (n.d.). Introduction to algorithms (3rd ed.).

I got many definitions, figures, graphs, code, etc. from this book--"Introduction to Algorithms", another worthwhile (whilst lengthy read) is Dr. Donald Knuth's books on the "Art of Computer Programming".
