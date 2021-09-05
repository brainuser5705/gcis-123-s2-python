"""
How can we make this code more efficient?
"""

import turtle

pen_c = "blue"
fill_c = "red"

# Draws first circle
turtle.pensize(0)
turtle.up()
turtle.goto(0,250)
turtle.down()
turtle.color(pen_c)
turtle.fillcolor(fill_c)
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.up()

# Draws second circle
turtle.pensize(0)
turtle.up()
turtle.goto(0,190)
turtle.down()
turtle.color(pen_c)
turtle.fillcolor(fill_c)
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.up()

# Draws third circle
turtle.pensize(0)
turtle.up()
turtle.goto(0,90)
turtle.down()
turtle.color(pen_c)
turtle.fillcolor(fill_c)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.up()

turtle.done()