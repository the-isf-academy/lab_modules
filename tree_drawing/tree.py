# tree.py

from turtle import *
from random import randint

# 💻 IMPORT MODULES BELOW  💻 #
from tree_parts import tree_trunk, tree_top 

# 💻 WRITE THE tree_full() FUNCTION BELOW  💻 #
def tree_full(size):
    tree_trunk(size)
    backward(size/4)
    tree_top(size)

def forest():
    for i in range (5):
        penup()
        x_coordinate = randint(-300,300) # generates a random integer between -200 and 200
        y_coordinate = randint(-200,200)
        goto(x_coordinate, y_coordinate)
        pendown()
        if (y_coordinate > 0): # if the tree is far
            tree_full(randint(50,100))
        else:
            tree_full(randint(100,200))

# 💻 DON'T FORGET TO CALL THE FUNCTION BELOW  💻 #
# tree_full(100)
speed(0)
forest()

input()