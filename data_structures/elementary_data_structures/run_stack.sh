#!/bin/sh
set -e

# Compile and execute Stack
g++ -Wall Stack.cpp -o stack.out
./stack.out
