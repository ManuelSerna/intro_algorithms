// Binary Search Tree (BST) Class Definition

#include "Node.h"

class BinarySearchTree
{
    private:
        int height; // length of longest branch in the BST
    public:
        Node *root;
        
        // Constructor and Destructor
    	BinarySearchTree();
    	~BinarySearchTree();
    	
    	// Printing
    	void InOrderWalk(Node *x); // inorder tree walk
    	void PreOrderWalk(Node *x); // preorder tree walk
    	void PostOrderWalk(Node *x); // postorder tree walk
        
        // Search-related operations
        Node *Search(Node *x, int k); // search starting at whatever node
        Node *Min(Node *x); // minimum of subtree
        Node *Max(Node *x); // maximum of subtree
        Node *Predecessor(Node *x); // predecessor of node
        Node *Successor(Node *x); // successor of node
        
        // Modify the tree
        void Transplant(Node *u, Node *v); // replace subtree rooted at u with subtree rooted at v
        void Insert(Node *z);
        void Delete(Node *z);
};
