//**********************************************
// Naive method for matrix multiplication.
/*
    Run time: Theta(n^3), very bad!
*/
//**********************************************

#include <iostream>
using namespace std;

const int N = 2;

//===============================================
// Initialize n * n matrix M.
//===============================================
void init_matrix(int M[][N])
{
    for (int i = 0; i < N; i++) 
    { 
        for (int j = 0; j < N; j++) 
        { 
            M[i][j] = 0;
        } 
    }
}

//===============================================
// Print function for a n * n matrix M.
//===============================================
void print_matrix(int M[][N])
{
    cout << endl;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << M[i][j] << " ";
        }
        
        cout << endl;
    }
}

//===============================================
// Naive implementation for matrix multiplication.
//===============================================
void matrix_multiply(int A[][N], int B[][N], int C[][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++) 
        {
            for (int k = 0; k < N; k++)
            {
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
}

//===============================================
// MAIN
//===============================================
int main()
{
    int A[N][N] = {{1, 0},
                   {0, 1}};
    int B[N][N] = {{1, 3},
                   {2, 4}};
    int C[N][N];
    
    init_matrix(C);
    print_matrix(A);
    print_matrix(B);
    
    matrix_multiply(A, B, C);
    
    print_matrix(C);
    
    return 0;
}
