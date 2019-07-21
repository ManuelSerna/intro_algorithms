//*********************************************** 
// Purpose: Implementation of Binary search tree class.
// Methods take in keys, not nodes
//***********************************************

#include "BinarySearchTree.h"

//===============================================
// Constructor and Destructor
//===============================================
BinarySearchTree::BinarySearchTree()
{
    // Root is nothing, with no values
    root = NULL;
}

BinarySearchTree::~BinarySearchTree()
{

}

//===============================================
// Print the entire tree--horizontally
//===============================================
#define COUNT 10

void printHelper(Node *x, int indent)
{
    if (x == NULL)  
        return;  
  
    indent += COUNT;  
  
    printHelper(x->right, indent);  

    cout << endl;  
    for (int i = COUNT; i < indent; i++)
    {
        cout << " ";  
    }
    cout<< x->key << endl;  

    printHelper(x->left, indent);
}

void BinarySearchTree::Print()
{
	cout << "--------------" << endl;
	cout << "Printing Tree." << endl;
	printHelper(root, 0);
	cout << "--------------" << endl;
}

//===============================================
// Traversals
//===============================================
void BinarySearchTree::Inorder(Node *x)
{
	if (x != NULL)
	{
		Inorder(x->left);
		cout << x->key << endl;
		Inorder(x->right);
	}
}

void BinarySearchTree::Preorder(Node *x)
{
	if (x != NULL)
	{
		cout << x->key << endl;
		Inorder(x->left);
		Inorder(x->right);
	}
}

void BinarySearchTree::Postorder(Node *x)
{
	if (x != NULL)
	{
		Inorder(x->left);
		Inorder(x->right);
		cout << x->key << endl;
	}
}

//===============================================
// Search Queries
//===============================================
Node *BinarySearchTree::Search(Node *x, int k)
{
	if (x != NULL || k != x->key)
	{
		return x;
	}
	if (k < x->key)
	{
		return Search(x->left, k);
	}
	else
	{
		return Search(x->right, k);
	}
}

Node *BinarySearchTree::SearchIterative(Node *x, int k)
{
	while (x != NULL && k != x->key)
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

Node *BinarySearchTree::Minimum(Node *x)
{
	while (x->left != NULL)
	{
		x = x->left;
	}
	return x;
}

Node *BinarySearchTree::Maximum(Node *x)
{
	while (x->right != NULL)
	{
		x = x->right;
	}
	return x;
}

Node *BinarySearchTree::Predecessor(Node *x)
{
	if (x->left != NULL)
	{
		return Maximum(x->left);
	}
	Node *y = x->parent;
	while (y != NULL && x == y->left)
	{
		x = y;
		y = y->parent;
	}
	return y;
}

Node *BinarySearchTree::Successor(Node *x)
{
	if (x->right != NULL)
	{
		return Minimum(x->right);
	}
	Node *y = x->parent;
	while (y != NULL && x == y->right)
	{
		x = y;
		y = y->parent;
	}
	return y;
}

//===============================================
// Insert
//===============================================
void BinarySearchTree::Insert(int key)
{cout << "inserting " << key << endl;
	// Create new node z and fill in key value from input
    Node *z = new Node;
    z->key = key;
    z->left = NULL;
    z->right = NULL;

	Node *y = NULL;
	Node *x = root;
	while (x != NULL)
	{
		y = x;
		if (z->key < x->key)
		{
			x = x->left; cout << "go left\n";
		}
		else
		{
			x = x->right; cout << "go right\n";
		}
	}
	z->parent = y; cout << "assign\n";
	if (y == NULL)
	{
		root = z;
	}
	else if (z->key < y->key)
	{
		y->left = z;
	}
	else
	{
		y->right = z;
	}
	cout << "Inserted key = " << key << endl;
}

//===============================================
// Delete
//===============================================
void BinarySearchTree::Transplant(Node *u, Node *v)
{
	if (u->parent == NULL)
	{
		root = v;
	}
	else if (u == u->parent->left)
	{
		u->parent->left = v;
	}
	else
	{
		u->parent->right = v;
	}
}

void BinarySearchTree::Delete(int key)
{
	// Create new node z (search first)
    Node *z = Search(root, key);

    if (z->left == NULL)
    {
    	Transplant(z, z->right);
    }
    else if (z->right == NULL)
    {
    	Transplant(z, z->left);
    }
    else
    {
    	Node *y = Minimum(z->right);
    	if (y->parent != z)
    	{
    		Transplant(y, y->right);
    		y->right = z->right;
    		y->right->parent = y;
    	}
    	Transplant(z, y);
    	y->left = z->left;
    	y->left->parent = y;
    }

    cout << "Deleted key = " << key << endl;
}
