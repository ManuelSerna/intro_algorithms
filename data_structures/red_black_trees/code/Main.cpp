// A simple program that allows users to create a red-black tree on the command line

#include "RedBlackTree.h"

int main()
{
    cout << "Red-black tree program." << endl;
    cout << "Select an action to perform, or exit." << endl;
    char choice = 'x';
    int input = 0;

    RedBlackTree Tree;

    while (true)
    {
        // Prompt user
        cout << "========================" << endl;
        cout << "i: Insert" << endl;
        cout << "d: Delete" << endl;
        cout << "p: Print" << endl;
        cout << "    1: Pre-order" << endl;
        cout << "    2: In-order" << endl;
        cout << "    3: Post-order" << endl;
        cout << "    4: Print tree (horizontal)" << endl;
        cout << "x: Exit" << endl;
        cout << "------------------------" << endl;
        cout << "Choice: ";
        cin >> choice;
        cout << "------------------------" << endl;

        switch(choice)
        {
            case 'i':
                cout << "Insert: ";
                cin >> input;
                Tree.Insert(input);
                break;
            case 'd':
                cout << "Delete: ";
                cin >> input;
                Tree.Delete(input);
                break;
            case 'p':
                cout << "\tWhat printing method? ";
                cin >> choice;
                switch(choice)
                {
                    case '1':
                        Tree.Preorder(Tree.Root());
                        break;
                    case '2':
                        Tree.Inorder(Tree.Root());
                        break;
                    case '3':
                        Tree.Postorder(Tree.Root());
                        break;
                    case '4':
                        Tree.Print();
                        break;
                }
                break;
            case 'x':
                cout << "Peacing out." << endl;
                return 0;
                break;
            default:
                cout << "Error: incorrect choice." << endl;
                break;
        }

        cout << "========================" << endl;
    }

    return 0;
}
