//***********************************************
// Test binary search tree implementation
//***********************************************
# include "BinarySearchTree.h"

using namespace std;

int main()
{
    cout << "Binary search tree program." << endl;
    BinarySearchTree Tree;

    /*
    We will make the following tree.
        14
       /  \
      7    18
     / \   / \
    2  11 17 20
    */

    // Insertion
    Tree.Insert(14);
    Tree.Print();
    
    Tree.Insert(7);
    Tree.Print();

    Tree.Insert(18);
    Tree.Print();

    Tree.Insert(2);
    Tree.Print();
    
    Tree.Insert(20);
    Tree.Print();

    Tree.Insert(11);
    Tree.Print();

    Tree.Insert(17);

    cout << "\n\nTree after insertions." << endl;
    Tree.Print();

    // Deletion
    Tree.Delete(14);
    Tree.Print();

    return 0;
}
