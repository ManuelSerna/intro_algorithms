//***********************************************
// Purpose: Header file for the Red Black Tree class.
//***********************************************

#include <iostream>
using namespace std;

//===============================================
// Data node definition.
//===============================================
class Node
{
    public:
    int key;
    char color;// Red = 'R', Black = 'B'
    Node *parent;
    Node *left;
    Node *right;

    Node(int k);
    ~Node();
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

    // Print the entire tree
    void printHelper(Node *x, int indent);
    void Print();

    // Traversal methods
    void Inorder(Node *x);
    void Preorder(Node *x);
    void Postorder(Node *x);

    // Queries used in this red-black tree
    Node *Search(Node *x, int k);
    Node *Minimum(Node *x);

    // Rotation methods
    void RotateLeft(Node *x);
    void RotateRight(Node *x);

    // Insertion-related methods
    void Insert(int key);
    void InsertFixup(Node *z);

    // Delete-related methods
    void Transplant(Node *u, Node *v);
    void Delete(int key);
    void DeleteFixup(Node *x);

    private:
    Node *root;
    Node *nil;
};
