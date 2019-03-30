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
A   B         RotateRight(y)             B   C  
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
/*
Four cases for fixing insertion:
    1. z is the root.
        - color z black
    2. z's parent is black.
        - black height still valid, do nothing
    3. z's parent is red and z's uncle is red.
        - recolor z's: parent, uncle, and grandparent to black, black, and red respectively.
    4. z is red and z's uncle is black.
        - goal: rotate z into its grandparent's position, to do this make z and its parent both right or both left subtrees to z's grandfather. Z and its former grandparent will both be red while z's parent will be black.
*/
//===============================================
void RedBlackTree::Insert(Node *z)
{
    Node *y = nil;
    Node *x = root;

    // Search the red-black tree to insert z (this is a normal insert)
    while (x != nil)
    {
        y = x;

        if (z->value < x->value)
        {
            x = x->left;
        }
        else
        {
            x = x->right;
        }
    }

    z->parent = y;// make y z's parent, and then check where z is relative to y

    if ( y == nil)
    {
        root = z;// tree empty
    }
    else if (z->value == y->value)
    {
        y->left = z;// insert left
    }
    else
    {
        y->right = z;// insert right
    }
    
    // Properly assign z's nil nodes, and always insert a red node
    z->left = nil;
    z->right = nil;
    z->color = 'R';

    // Maintain red-black properties
    InsertFixup(z);
}

void RedBlackTree::InsertFixup(Node *z)
{
    if (Parent(z) == nil)
    {
        if(Parent(z) == nil)
        {
            z->color = 'B';
        }
    }
    else if (Parent(z)->color == 'B')
    {
        // No red-black properties violated
        return;
    }
    else if (Uncle(z) != nil && Uncle(z)->color == 'R')
    {
        Parent(z)->color = 'B';
        Uncle(z)->color = 'B';
        Grandparent(z)->color = 'R';

        // Grandparent may now violate condition that root is black or that it may be the red child of a red parent
        InsertFixup(Grandparent(z));
    }
    else
    {
        Node *p = Parent(z);
        Node *g = Grandparent(z);

        // Ensure that z and its parent are outer nodes in the tree
        if (z == p->right && p == g->left)
        {
            RotateLeft(p);
            z = z->left;
        }
        else if (z == p->left && p->right)
        {
            RotateRight(p);
            z = z->right;
        }

        // Now that node z and its parent are both right or both left children, rotate the grandparent the opposite direction of z
        if (z == p->left)
        {
            RotateRight(g);
        }
        else
        {
            RotateLeft(g);
        }

        p->color = 'B';
        g->color = 'R';
    }
}

//===============================================
// TODO: implement delete methods
//===============================================
