#!/bin/sh
set -e

echo "Executing sorting algorithms"
echo "*****************************"
echo ""
echo ""
echo "Insertion sort"
echo "------------------"
python3 insertion_sort.py
echo ""
echo ""
echo "Merge sort"
echo "------------------"
python3 merge_sort.py
echo ""
echo ""
echo "Done."
