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
    Node *parent;
    Node *left;
    Node *right;
};

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
    Node *Grandparent(Node *n);
    Node *Sibling(Node *n);
    Node *Uncle(Node *n);

    // Rotation methods
    void RotateLeft(Node *x);
    void RotateRight(Node *x);

    // Insertion-related methods, divide fixup into the four cases
    void Insert(Node *n);
    void InsertHelper(Node *n);
    void InsertFixup(Node *n);
    void InsertCase1(Node *n);
    void InsertCase2(Node *n);
    void InsertCase3(Node *n);
    void InsertCase4(Node *n);

    // Delete-related methods
    // TODO: define and later implement

    private:
    Node *root;
    Node *nil;
};