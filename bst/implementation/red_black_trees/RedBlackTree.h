//***********************************************
// Purpose: Header file for the Red Black Tree class.
// Author:  Manuel Serna-Aguilera 
//***********************************************

#include <iostream>
using namespace std;

//===============================================
// Data node definition.
//===============================================
class Node
{
    public:
    int value;
    char color;// Red = 'R', Black = 'B'
    Node *Parent;
    Node *Left;
    Node *Right;
}

//===============================================
// Define the Red Black tree class interface.
//===============================================
class RedBlackTree
{
    public:
    // Constructor and Destructor
    RedBlackTree();
    ~RedBlackTree();

    // Return nodes related to a node n
    Node *Parent(Node *n);
    Node *Grandfather(Node *n);
    Node *Sibling(Node *n);
    Node *Uncle(Node *n);

    // Rotation methods
    void RotateLeft(Node *n);
    void RotateRight(Node *n);

    // Insertion-related methods, divide fixup into the four cases
    Node *Insert(Root, Node *n);
    void InsertHelper(Root, Node *n);
    void InsertFixup(Node *n);
    void InsertCase1(Node *n);
    void InsertCase2(Node *n);
    void InsertCase3(Node *n);
    void InsertCase4(Node *n);

    // Delete-related methods
    // TODO: define and later implement

    private:
    Node *Root;
}