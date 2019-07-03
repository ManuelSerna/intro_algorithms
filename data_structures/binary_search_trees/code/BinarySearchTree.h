//***********************************************
// Purpose: Header file for the Binary Search Tree class.
//***********************************************

#include <iostream>
#include <iomanip>
using namespace std;

//===============================================
// Data node definition.
//===============================================
class Node
{
    public:
    int key;
    Node *parent;
    Node *left;
    Node *right;
};

//===============================================
// Define the Binary Search Tree class interface.
//===============================================
class BinarySearchTree
{
    public:
    	// Constructor and Destructor
    	BinarySearchTree();
    	~BinarySearchTree();

        // Print the entire tree
        void Print();

    	// Traversal methods
    	void Inorder(Node *x);
    	void Preorder(Node *x);
    	void Postorder(Node *x);

    	// Search queries
    	Node *Search(Node *x, int k);
    	Node *SearchIterative(Node *x, int k);
    	Node *Minimum(Node *x);
    	Node *Maximum(Node *x);
    	Node *Predecessor(Node *x);
    	Node *Successor(Node *x);

    	void Insert(int key);

    	void Transplant(Node *u, Node *v);
    	void Delete(int key);

    private:
    	Node *root;
};
