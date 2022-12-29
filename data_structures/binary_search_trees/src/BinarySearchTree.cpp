// Binary Search Tree Class Implementation

#include "BinarySearchTree.h"

#include <iostream>

using namespace std;

//================================
// Constructor and Destructor
//================================
BinarySearchTree::BinarySearchTree()
{
    height = 0;
    root = NULL;
}

BinarySearchTree::~BinarySearchTree()
{
}

//================================
// Walking functions
//================================
void BinarySearchTree::InOrderWalk(Node *x)
{
    if (x != NULL)
    {
        InOrderWalk(x->left);
        cout << x->key << " ";
        InOrderWalk(x->right);
    }
}

void BinarySearchTree::PreOrderWalk(Node *x)
{
    if (x != NULL)
    {
        cout << x->key << " ";
        PreOrderWalk(x->left);
        PreOrderWalk(x->right);
    }
}

void BinarySearchTree::PostOrderWalk(Node *x)
{
    if (x != NULL)
    {
        PostOrderWalk(x->left);
        PostOrderWalk(x->right);
        cout << x->key << " ";
    }
}

//================================
// Search for a node with a certain key, otherwise return NULL
//================================
Node *BinarySearchTree::Search(Node *x, int k)
{
    while (x != NULL && x->key != k)
    {
        if (k < x->key) x = x->left;
        else if (k > x->key) x = x->right;
    }
    
    return x;
}

//================================
// Find minimum of subtree
//================================
Node *BinarySearchTree::Min(Node *x)
{
    while (x->left != NULL)
    {
        x = x->left;
    }
    
    return x;
}

//================================
// Find maximum of subtree
//================================
Node *BinarySearchTree::Max(Node *x)
{
    while (x->right != NULL)
    {
        x = x->right;
    }
    
    return x;
}

//================================
// Predecessor of a node
//================================
Node *BinarySearchTree::Predecessor(Node *x)
{
    if (x->left != NULL)
    {
        // Node has a left child, so get max of left subtree
        return Max(x->left);
    }
    else
    {
        // No left child, so we get parent of first node that's a right child
        Node *y = x->parent;
        
        while (x != NULL && y->left == x)
        {
            x = y;
            y = y->parent;
        }
        
        return y;
    }
}

//================================
// Successor of a node
//================================
Node *BinarySearchTree::Successor(Node *x)
{
    if (x->right != NULL)
    {
        // Node has a right child, so get min of *right* subtree
        return Min(x->right);
    }
    else
    {
        // No right child, so we get the parent of the first node that's a *left* child
        Node *y = x->parent;
        
        while (x != NULL && y->right == x)
        {
            x = y;
            y = y->parent;
        }
        
        return y;
    }
}

//================================
//================================
void BinarySearchTree::Transplant(Node *u, Node *v)
{
}

//================================
// Insert a new node into the BST
//================================
void BinarySearchTree::Insert(Node *z)
{
    Node *y = NULL; // keep track of the x's parent (root->parent = NULL)
    Node *x = root; // always start at the root
    
    // Search
    while (x != NULL)
    {
        y = x; // keep track of parent node
        
        if (z->key < x->key) x = x->left;
        else if (z->key > x->key) x = x->right;
    }
    
    z->parent = y;
    
    // Insert
    if (y == NULL) { root = z; } // tree was empty
    else if (z->key < y->key) { y->left = z; } // insert as left child
    else if (z->key > y->key) { y->right = z; } // insert as right child
}

//================================
//================================
void BinarySearchTree::Delete(Node *z)
{
}

