// Test Binary Search Tree

#include "BinarySearchTree.h"

using namespace std;

int main()
{
    BinarySearchTree tree;
    
    // Insert nodes for below tree
    /*
           7
         /  \
        4   10
       / \  /
      3  5 9
     /    /
    1    8
    */
    tree.Insert(new Node(7));
    tree.Insert(new Node(4));
    tree.Insert(new Node(5));
    tree.Insert(new Node(3));
    tree.Insert(new Node(10));
    tree.Insert(new Node(9));
    tree.Insert(new Node(1));
    tree.Insert(new Node(8));
    
    
    // Walking functions
    tree.InOrderWalk(tree.root); cout << endl;
    
    tree.PreOrderWalk(tree.root); cout << endl;
    
    tree.PostOrderWalk(tree.root); cout << endl;
    
    
    // Query nodes
    Node *x = tree.Search(tree.root, 8);
    if (x != NULL) { cout << "Found node key: " << x->key <<endl; }
    
    x = tree.Search(tree.root, 6);
    if (x != NULL) { cout << "Found node key: " << x->key <<endl; }
    else { cout << "Node with key=" << 6 << " not found!" << endl; }
    
    x = tree.Min(tree.root);
    if (x != NULL) { cout << "Min: " << x->key << endl; }
    
    x = tree.Max(tree.root);
    if (x != NULL) { cout << "Max: " << x->key << endl; }
    
    
    // Predecessor
    x = tree.Search(tree.root, 7);
    x = tree.Predecessor(x);
    if (x != NULL) { cout << "Predecessor(7)=" << x->key << endl; }
    
    x = tree.Search(tree.root, 8);
    x = tree.Predecessor(x);
    if (x != NULL) { cout << "Predecessor(8)=" << x->key << endl; }
    
    x = tree.Search(tree.root, 5);
    x = tree.Predecessor(x);
    if (x != NULL) { cout << "Predecessor(5)=" << x->key << endl; }
    
    // Successor
    x = tree.Search(tree.root, 7);
    x = tree.Successor(x);
    if (x != NULL) { cout << "Successor(7)=" << x->key << endl; }
    
    x = tree.Search(tree.root, 8);
    x = tree.Successor(x);
    if (x != NULL) { cout << "Successor(8)=" << x->key << endl; }
    
    x = tree.Search(tree.root, 5);
    x = tree.Successor(x);
    if (x != NULL) { cout << "Successor(5)=" << x->key << endl; }
    
    
    // Delete
    /* delete(1) =>
           7
         /  \
        4   10
       / \  /
      3  5 9
          /
         8
    */
    cout << "delete(1):" << endl;
    Node *z = tree.Search(tree.root, 1);
    tree.Delete(z);
    tree.InOrderWalk(tree.root); cout << endl;
    
    /* delete(10) =>
           7
         /   \
        4    9
       / \  /
      3  5 8
    */
    cout << "delete(10):" << endl;
    z = tree.Search(tree.root, 10);
    tree.Delete(z);
    tree.InOrderWalk(tree.root); cout << endl;
    
    /* delete(7) =>
           8
         /   \
        4    9
       / \
      3  5
    */
    cout << "delete(7):" << endl;
    z = tree.Search(tree.root, 7);
    tree.Delete(z);
    tree.InOrderWalk(tree.root); cout << endl;
    
    return 0;
}
