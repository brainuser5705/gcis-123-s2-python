import turtle as t

"""
These are helper functions that draw the basic shapes needed to make the trees.
"""

def draw_circle(color, rad):
    t.color(color)
    t.fillcolor(color)
    t.down()
    t.seth(0)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

def draw_triangle(color, len):
    t.color(color)
    t.fillcolor(color)
    t.down()
    t.seth(180)

    t.begin_fill()
    t.right(120)
    t.fd(len)
    t.right(120)
    t.fd(len)
    t.right(120)
    t.fd(len)
    t.end_fill()

def draw_rectangle(color, len, wid):
    t.color(color)
    t.fillcolor(color)
    t.down()
    t.seth(270)

    t.begin_fill()
    t.fd(len)
    t.left(90)
    t.fd(wid)
    t.left(90)
    t.fd(len)
    t.left(90)
    t.fd(wid)
    t.end_fill()

    t.seth(90) # to re-orient the turtle for next drawing phase