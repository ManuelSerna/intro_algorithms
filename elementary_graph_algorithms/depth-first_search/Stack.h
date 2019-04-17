//*********************************************** 
// Purpose: Header file for stack class.
// Author:  Manuel Serna-Aguilera
//*********************************************** 
#include <iostream>
using namespace std;
const int LENGTH = 100;

class Stack
{
public:
    // Constructor and Destructor
    Stack();
    ~Stack();
    
    // Basic stack operations
    bool Empty();
    bool Full();
    void Push(int x);
    int  Pop();
    void Print();
private:
    int S[LENGTH];
    int Top;
};
