// Node Class Implementation

#include "Node.h"

Node::Node(int k)
{
    key = k;
    parent = NULL;
    left = NULL;
    right = NULL;
}

Node::~Node()
{
}
