//*********************************************** 
// Purpose: Implementation of stack class.
// Author:  Manuel Serna-Aguilera
//***********************************************
#include "Stack.h"

//-----------------------------------------------
// Constructor.
//-----------------------------------------------
Stack::Stack()
{
    Top = 0;
    
    for(int i = 0; i < LENGTH; i++)
    {
        S[i] = 0;
    }
}

//-----------------------------------------------
// Destructor.
//-----------------------------------------------
Stack::~Stack()
{
}

//-----------------------------------------------
// Check if the stack is empty.
//-----------------------------------------------
bool Stack::Empty()
{
    return Top < 0;
}

//-----------------------------------------------
// Check if the stack is full.
//-----------------------------------------------
bool Stack::Full()
{
    return Top < LENGTH;
}

//-----------------------------------------------
// Push, or insert, a new value to the stack.
//-----------------------------------------------
void Stack::Push(int x)
{
    // Check if stack is full.
    if(Top == LENGTH)
        return;
    
    S[Top] = x;
    Top++;
}

//-----------------------------------------------
// Pop, or remove, values from the stack.
//-----------------------------------------------
int Stack::Pop()
{
    if(Empty())
    {
        cout << "Error: underflow." << endl;
        return -1;
    }
    else
    {
        Top--;
        int x = S[Top];
        S[Top] = 0;
        return x;
    }
}

//-----------------------------------------------
// Print all records in the stack.
//-----------------------------------------------
void Stack::Print()
{
    cout << "Printing stack: ";
    for(int i = 0; i < Top; i++)
    {
        cout << S[i] << " ";
    }
    cout << endl;
    
    /*
    for(int i = 0; i < LENGTH; i++)
    {
        cout << S[i] << " ";
    }
    */
}
