//*********************************************** 
// Purpose: Implementation of Red Black tree class.
// Author:  Manuel Serna-Aguilera
//***********************************************

#include "RedBlackTree.h"

//===============================================
// Constructor and Destructor
//===============================================
RedBlackTree::RedBlackTree()
{
    // Define nil for black null leafs
    nil = NULL;

    // Root is nothing, with no values
    root = NULL;
    root->parent = nil;
    root->left = nil;
    root->right = nil;
}

RedBlackTree::~RedBlackTree()
{

}

//===============================================
// Nodes related to any node n.
//===============================================
Node *RedBlackTree::Parent(Node *n)
{
    return n->parent;
}

Node *RedBlackTree::Grandparent(Node *n)
{
    Node* p = Parent(n);

    // No parent means no grandparent
    if (p == NULL)
    {
        return NULL;
    }

    return Parent(p);// note: null if the parent is the root
}

Node *RedBlackTree::Sibling(Node *n)
{
    Node *p = Parent(n);
    
    if (p == NULL)
    {
        return NULL; // no parent means no sibling
    }

    if (n == p->left)
    {
        return p->right;
    }

    else
    {
        return p->left;
    }
}

Node *RedBlackTree::Uncle(Node *n)
{
    Node *p = Parent(n);
    Node *g = Grandparent(n);

    if (g == NULL)
    {
        return NULL; // No grandparent means no uncle
    }

    return Sibling(p);
}

//===============================================
// Rotation operations.
/*
A visual:

    |         RotateLeft(x)              |
    y         <----------------          x
   / \                                  / \
  x   C                                A   y
 / \          ---------------->           / \
A   B         RotateRIght(y)             B   C  
*/
//===============================================
void RedBlackTree::RotateLeft(Node *x)
{
    Node *y = x->right;// set y to be x's right child
    x->right = y->left;// turn y's left subtree (B) into x's right

    // If B is a populated subtree, have x point to it
    if (y->left != nil)
    {
        y->left->parent = x;// 
    }

    // Link x's parent to y
    y->parent = x->parent;

    // Make y the new root if x was the root
    if (x->parent == nil)
    {
        root = x;
    }
    else if (y == y->parent->right)
    {
        y->parent->right = x;// make y the right child of x
    }
    else
    {
        y->parent->left = x;// make x the left child of y
    }

    x->right = y;// put y on x's right
    y->parent = x;
}

void RedBlackTree::RotateRight(Node *y)
{
    Node *x = y->left;// set x to be y's right child
    y->left = x->right;// turn x's left subtree (B) into y's right subtree

    // If B is a populated subtree, have y point to x
    if (x->right != nil)
    {
        x->right->parent = y;
    }

    x->parent = y->parent;// link x's parent to y

    // Make x the new root if y was the root
    if (y->parent == nil)
    {
        root = x;
    }
    else if (y == y->parent->right)
    {
        y->parent->right = x;// make y the right child of x
    }
    else
    {
        y->parent->left = x;// make y the left child of x
    }

    x->right = y;// put y on x's right
    y->parent = x;
    
}

//===============================================
// Insert method and recursive helper.
//===============================================
void RedBlackTree::Insert(Node *n)
{

}

void RedBlackTree::InsertHelper(Node *n)
{

}

void RedBlackTree::InsertFixup(Node *n)
{

}

//===============================================
/*
Insertion cases:
    i.   x
    ii.  x
    iii. x
    iv.  x
*/
//===============================================
void RedBlackTree::InsertCase1(Node *n)
{

}

void RedBlackTree::InsertCase2(Node *n)
{

}

void RedBlackTree::InsertCase3(Node *n)
{

}

void RedBlackTree::InsertCase4(Node *n)
{

}

//===============================================
// TODO: implement delete methods
//===============================================