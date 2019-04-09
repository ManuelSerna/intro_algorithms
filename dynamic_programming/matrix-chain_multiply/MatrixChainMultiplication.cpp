//***********************************************
/* 
    Matrix chain multiplication algorithm.
        - utilizes dyanmic programming--bottom-up approach.
        
    Tables:
        - m: holds the optimal costs for multiplying a sequence of n matrices.
            - m[1][n] will hold the optimal solution.
        - s: holds, according to what sequence of matrices in m gives the lowest cost,
        s will contain the "cut-off" point after matrix i (see scanned document for a clearer ex).
        
    Note: the m and s 2D arrays will take n^2 space, but they will only use at most half.
*/
//***********************************************
#include <iostream>
using namespace std;

// Number of matrices, or length of sequence
const int N = 4;

//-----------------------------------------------
// Initialize elements in some 2D array to be zeros.
//-----------------------------------------------
void init2DArray(int a[][N])
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            a[i][j] = -1;
        }
    }
}

//-----------------------------------------------
// Print contents of 2D array.
//-----------------------------------------------
void print2DArray(int a[][N])
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            cout << a[i][j];
        }
        
        cout << endl;
    }
}

//-----------------------------------------------
// Calculate the optimal sequence of matrices giving minimum cost.
//-----------------------------------------------
void matrixChainOrder(int p[], int m[][N], int s[][N])
{
    // Cost of having one matrix is zero (mutliplying matrix with nothing)
    for(int i = 0; i < N; i++)
    {
        m[i][i] = 0;
    }
    
    // Now, first, start calculating costs for all pairs of matrices
    for(int 
}


//-----------------------------------------------
// MAIN
//-----------------------------------------------
int main()
{
    // Sequence of dimensions between adjacent matrices in the sequence
    int dimSequence = {5, 4, 6, 2, 7};
    
    // Table m for optimal values given a subsequence of i matrices (0 <= i <= n)
    int m[N][N];
    init2DArray(m);
    
    // Table for cutting of sequences in order to get minimum cost
    int s[N][N];
    init2DArray(s);
    
    cout << "Sequence of " << N << " arrays." << endl;
    matrixChainOrder(dimSequence, m, s);
    
    return 0;
}
