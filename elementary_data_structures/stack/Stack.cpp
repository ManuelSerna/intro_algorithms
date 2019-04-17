//***********************************************
// Stack implementation.
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

//-----------------------------------------------
// MAIN
//-----------------------------------------------
int main()
{
    Stack stack;
    
    stack.Push(1);
    stack.Push(2);
    stack.Push(3);
    stack.Print();
    
    int y = stack.Pop();
    int z = stack.Pop();
    
    cout << "Values popped.\n";
    cout << y << " " << z << endl;
    
    stack.Print();
    
    return 0;
}
