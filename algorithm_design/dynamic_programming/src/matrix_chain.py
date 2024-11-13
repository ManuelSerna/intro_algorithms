import numpy as np

infty = 999999

def matrix_chain_order(dims:list):
    n = len(dims)-1
    cost = np.zeros((n,n))
    split = np.zeros((n,n))

    for chain_len in range(2,n+1):
        # Iterate over chain length

        for i in range(0, n-chain_len+1):
            # Iterate over row i
            
            # Index j goes over column j
            j = i+chain_len-1 # Consider sequence A_i ... A_j
            cost[i,j] = infty

            for k in range(i, j):
                """
                - The cost indexing is referring to the cost of the subsequence

                cost[i,k]: cost of smaller subsequence (A_i, ..., A_k)
                cost[k+1,j]: cost of smaller subsequence (A_{k+1}, ..., A_j)

                - The dims refer to the cost of the current-length sequence

                  A_i, ...., A_j
                """
                q = cost[i,k] + cost[k+1,j] + (dims[i] * dims[k+1] * dims[j+1])

                print(f"{q} = {cost[i,k]} + {cost[k+1,j]} + {dims[i]} * {dims[k+1]} * {dims[j+1]}")

                if q < cost[i,j]:
                    cost[i,j] = q
                    split[i,j] = k+1
    
    print("Cost:\n",cost)
    print("Splits:\n",split)

def main():
    #dims = [5,4,6,2,7]
    #dims = [30,35,15,5,10,20,25]
    #dims = [20,5,40,50,10]
    dims = [4,2,3,5,4]
    matrix_chain_order(dims)

if __name__ == "__main__":
    main()
