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
        cout << "x: Exit" << endl;
        cout << "------------------------" << endl;
        cout << "Input: ";
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
                break;
            case 'p':
                cout << "Printing." << endl;
                Tree.Print();
                break;
            case 'x':
                cout << "Peacing out." << endl;
                return 0;
                break;
            default:
                cout << "Error: incorrect input." << endl;
                break;
        }

        cout << "========================" << endl;
    }
    
    return 0;
} 
