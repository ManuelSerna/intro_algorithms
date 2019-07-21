//***********************************************
// Purpose: Implementation of Red Black tree class.
//***********************************************

#include "RedBlackTree.h"

//===============================================
// Constructors and Destructors
//===============================================
// Define node constructor for easy creation
Node::Node(int k)
{
    key    = k;
    parent = NULL;
    left   = NULL;
    right  = NULL;
    color  = 'R';
}
Node::~Node()
{
}

RedBlackTree::RedBlackTree()
{
    // Make nil sentinel, it must be black, other attributes may be arbritrary
    nil         = new Node(-1);
    nil->color  = 'B';
    nil->parent = nil;
    nil->left   = nil;
    nil->right  = nil;

    // Start empty tree with the nil sentinel
    root = nil;
}

RedBlackTree::~RedBlackTree()
{

}

//===============================================
// Nodes related to any node n.
//===============================================
Node *RedBlackTree::Root()
{
    return root;
}

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
        return NULL; // no grandparent means no uncle
    }

    return Sibling(p);
}

//===============================================
// Print tree horizontally. Nil nodes will not be printed.
//===============================================
#define COUNT 10

void RedBlackTree::printHelper(Node *x, int indent)
{
    if (x == NULL || x == nil)
        return;

    indent += COUNT;

    printHelper(x->right, indent);

    cout << endl;
    for (int i = COUNT; i < indent; i++)
    {
        cout << " ";
    }
    cout<< x->key << x->color << endl;

    printHelper(x->left, indent);
}

void RedBlackTree::Print()
{
    printHelper(root, 0);
}

//===============================================
// Traversals
//===============================================
void RedBlackTree::Inorder(Node *x)
{
    if (x != nil)
    {
        Inorder(x->left);
        cout << x->key << x->color << endl;
        Inorder(x->right);
    }
}

void RedBlackTree::Preorder(Node *x)
{
    if (x != nil)
    {
        cout << x->key << x->color << endl;
        Inorder(x->left);
        Inorder(x->right);
    }
}

void RedBlackTree::Postorder(Node *x)
{
    if (x != nil)
    {
        Inorder(x->left);
        Inorder(x->right);
        cout << x->key << x->color << endl;
    }
}

//===============================================
// Queries (look at BST implementation for the other ones)
//===============================================
Node *RedBlackTree::Search(Node *x, int k)
{
    while (x != nil && k != x->key)
    {
        if (k < x->key)
        {
            x = x->left;
        }
        else
        {
            x = x->right;
        }
    }

    return x;
}

Node *RedBlackTree::Minimum(Node *x)
{
    while (x->left != nil)
    {
        x = x->left;
    }
    return x;
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
    Node *y = x->right;// set y to be x's right child (initially)
    x->right = y->left;// turn y's left subtree (B) into x's right subtree

    // If subtree B is populated, have x point to it
    if (y->left != nil)
    {
        y->left->parent = x;
    }

    // Let y point to x's (to be former) parent
    y->parent = x->parent;

    // Make y the new root if x was the root
    if (x->parent == nil)
    {
        root = y;
    }
    else if (x == x->parent->left)
    {
        x->parent->left = y;// make y its new parent's left child
    }
    else
    {
        x->parent->right = y;// ..otherwise y is a right child
    }

    y->left = x;// put x on y's left
    x->parent = y;// y is x's new parent
}

void RedBlackTree::RotateRight(Node *y)
{
    Node *x = y->left;// set x to be y's left child
    y->left = x->right;// turn x's right subtree (B) into y's left subtree

    // If subtree B is populated, have y point to it
    if (x->right != nil)
    {
        x->right->parent = y;
    }

    // Let x point to y's (to be former) parent
    x->parent = y->parent;

    // Make x the new root if y was the root
    if (y->parent == nil)
    {
        root = x;
    }
    else if (y == y->parent->right)
    {
        y->parent->right = x;// make x its new parent's left child
    }
    else
    {
        y->parent->left = x;// ..otherwise x is a right child
    }

    x->right = y;// put y on x's right
    y->parent = x;// x is y's new parent
}

//===============================================
// Insert method and recursive helper.
/*
Four cases for fixing insertion for this method:
    1. z is the root.
        - color z black
    2. z's parent is black.
        - black height still valid, do nothing
    3. z's parent is red and z's uncle is red.
        - recolor z's: parent, uncle, and grandparent
        to black, black, and red respectively.
    4. z is red and z's uncle is black.
        - goal: rotate z into its grandparent's position,
        to do this make z and its parent both right or both left subtrees
        to z's grandfather.
        Z and its former grandparent will both be red
        while z's parent will be black.
*/
//===============================================
void RedBlackTree::Insert(int key)
{
    // Create new node z and fill in value from input
    Node *z = new Node(key);

    Node *y = nil;
    Node *x = root;

    // Search the red-black tree to insert z (this is a normal insert)
    while (x != nil)
    {
        y = x;

        if (z->key < x->key)
        {
            x = x->left;
        }
        else
        {
            x = x->right;
        }
    }

    z->parent = y;// make y z's parent, and then check where z is relative to y

    if (y == nil)
    {
        root = z;// tree empty
        root->parent = nil;// have root point to nil as its parent
    }
    else if (z->key < y->key)
    {
        y->left = z;// insert left
    }
    else
    {
        y->right = z;// insert right (also inserts duplicates right)
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
    while (z->parent->color == 'R')
    {
        if (z->parent == Grandparent(z)->left)
    	{
            Node *y = Uncle(z);// get uncle

            // Case 1: uncle (y) is red
    		if (y->color == 'R')
    		{
                Node *g = Grandparent(z);// get grandparent of this z
    			z->parent->color = 'B';
    			y->color = 'B';
                g->color = 'R';
                z = g;
    		}
    		else
    		{
                // Case 2: "triangle" case
    			if (z == z->parent->right)
    			{
    				z = z->parent;
    				RotateLeft(z);
    			}
                Node *g = Grandparent(z); // after any rotations, get current z's grandparent

                // Case 3: "line" case
    			z->parent->color = 'B';
                g->color = 'R';
                RotateRight(g);
    		}
    	}
    	// Symmetric case, exchange "left" with "right" below
    	else
    	{
            Node *y = Grandparent(z)->left;

            // Case 1: uncle (y) is red
    		if (y->color == 'R')
    		{
                Node *g = Grandparent(z);// get grandparent of this z
    			z->parent->color = 'B';
    			y->color = 'B';
                g->color = 'R';
                z = g;
    		}
    		else
    		{
                // Case 2: "triangle" case
    			if (z == z->parent->left)
    			{
    				z = z->parent;
    				RotateRight(z);
    			}
                Node *g = Grandparent(z); // after any rotations, get current z's grandparent

                // Case 3: "line" case
    			z->parent->color = 'B';
                g->color = 'R';
                RotateLeft(g);
    		}
    	}
    }
    
    root->color = 'B';// maintain root as a black node
}

//===============================================
// Delete methods.
//===============================================

// Replace subtree rooted at u with subtree rooted at v
void RedBlackTree::Transplant(Node *u, Node *v)
{
    if (u->parent == nil)
    {
        root = v;// u is the root, replace it with v
    }
    else if (u == u->parent->left)
    {
        u->parent->left = v;// u was a left subtree, replace it with v
    }
    else
    {
        u->parent->right = v;// u was a right subtree, replace it with v
    }

    v->parent = u->parent;// link v to u's parent, replacemet complete
}

void RedBlackTree::Delete(int key)
{
    Node *z = Search(root, key);// search node z to delete
    Node *y = z;
    Node *x = NULL;

    char yOriginalColor = y->color;

    // No-child and single-child cases: 
    //  - either replace z with its non-nil subtree, or
    //  - replace z with a nil node.
    if (z->left == nil)
    {
        x = z->right;
        Transplant(z, z->right);
    }
    else if (z->right == nil)
    {
        x = z->left;
        Transplant(z, z->left);
    }

    // Two-children case: find z's successor y to replace z. 
    // Some node x will replace y, the problems by moving x will be fixed in the DeleteFixup method
    else
    {
        y = Minimum(z->right);
        yOriginalColor = y->color;
        x = y->right;

        if (y->parent == z)
        {
            x->parent = y;
        }
        else
        {
            Transplant(y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }

        Transplant(z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }

    // If node that was replaced was black, fix potential violations
    if (yOriginalColor == 'B')
    {
        DeleteFixup(x);
    }
}

void RedBlackTree::DeleteFixup(Node *x)
{
    while (x != root && x->color == 'B')
    {
        if (x == x->parent->left)
        {
            // x's sibling w
            Node *w = x->parent->right;

            // Delete fixup case 1
            if (w->color == 'R')
            {
                w->color = 'B';
                x->parent->color = 'R';
                RotateLeft(x->parent);
                w = x->parent->right;
            }

            // Delete fixup case 2
            if (w->left->color == 'B' && w->right->color == 'B')
            {
                w->color = 'R';
                x = x->parent;
            }

            // Delete fixup cases 3 and 4
            else
            {
                // Case 3
                if (w->right->color == 'B')
                {
                    w->left->color = 'B';
                    w->color = 'R';
                    RotateRight(w);
                    w = x->parent->right;
                }

                // Continue with case 4
                w->color = x->parent->color;
                x->parent->color = 'B';
                w->right->color = 'B';
                RotateLeft(x->parent);
                x = root;
            }
        }

        // Symmetric case, exchange "left" with "right" below
        else
        {
            // x's sibling w
            Node *w = x->parent->left;

            // Delete fixup case 1
            if (w->color == 'R')
            {
                w->color = 'B';
                x->parent->color = 'R';
                RotateRight(x->parent);
                w = x->parent->left;
            }

            // Delete fixup case 2
            if (w->right->color == 'B' && w->left->color == 'B')
            {
                w->color = 'R';
                x = x->parent;
            }

            // Delete fixup cases 3 and 4
            else
            {
                // Case 3
                if (w->left->color == 'B')
                {
                    w->right->color = 'B';
                    w->color = 'R';
                    RotateLeft(w);
                    w = x->parent->left;
                }

                // Continue with case 4
                w->color = x->parent->color;
                x->parent->color = 'B';
                w->left->color = 'B';
                RotateRight(x->parent);
                x = root;
            }
        }
    }

    x->color = 'B';
}
