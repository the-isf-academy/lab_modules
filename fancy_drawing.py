# fancy_drawing.py


from turtle import *
from drawing.shapes import *
from drawing.movement import *
from drawing.lines import *



# 💻 Create a drawing of your choosing BELOW  💻 #
pensize(10)
with rainbow():
    for i in range(10, 100, 10):
        circle(i)
        penup()
        x, y = position()
        sety(y - 10)
        pendown()