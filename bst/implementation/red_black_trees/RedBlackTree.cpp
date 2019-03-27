//*********************************************** 
// Purpose: Implementation of Red Black tree class.
// Author:  Manuel Serna-Aguilera
//***********************************************

#import "RedBlackTree.h"

//===============================================
// Constructor and Destructor
//===============================================
RedBlackTree::RedBlackTree()
{
    Root = NULL;
}

RedBlackTree::~RedBlackTree()
{

}

//===============================================
// Nodes related to any node n.
//===============================================
Node *RedBlackTree::Parent(Node *n)
{
    return n->Parent;
}

Node *RedBlackTree::Grandfather(Node *n)
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
    Node* p = Parent(n);
    
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
    Node* p = Parent(n);
    Node* g = Grandparent(n);

    if (g == NULL)
    {
        return NULL; // No grandparent means no uncle
    }

    return Sibling(p);
}

//===============================================
// Rotation operations.
//===============================================
void RedBlackTree::RotateLeft(Node *n)
{

}

void RedBlackTree::RotateRight(Node *n)
{

}

//===============================================
// Insert method and recursive helper.
//===============================================
Node *RedBlackTree::Insert(Root, Node *n)
{

}

void RedBlackTree::InsertHelper(Root, Node *n)
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