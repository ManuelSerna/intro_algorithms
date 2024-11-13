// Node Class Definition

#include <iostream>

class Node
{
    private:
    public:
        int key;
        
        Node *parent;
        Node *left;
        Node *right;
        
        Node(int k);
        ~Node();
};
