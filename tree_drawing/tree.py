# tree.py

from turtle import *
from tree_parts import tree_trunk, tree_top 


def tree_full(size):
    tree_trunk(size)
    backward(size/4)
    tree_top(size)


tree_full(100)

input()







