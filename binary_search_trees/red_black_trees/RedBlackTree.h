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
    Node *Root();
    Node *Parent(Node *n);
    Node *Grandparent(Node *n);
    Node *Sibling(Node *n);
    Node *Uncle(Node *n);

    // Printing method
    void Print();
    void Inorder(Node *x);

    // Rotation methods
    void RotateLeft(Node *x);
    void RotateRight(Node *x);

    // Insertion-related methods
    void Insert(int value);
    void InsertFixup(Node *z);

    // Delete-related methods
    void Transplant(Node *u, Node *v);
    void Delete(int value);
    void DeleteFixup(Node *x);

    private:
    Node *root;
};