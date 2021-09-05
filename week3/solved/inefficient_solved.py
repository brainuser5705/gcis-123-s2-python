"""

"""
import turtle as t

pen_c = "blue"
fill_c = "red"

STARTING_SIZE = 10
STARTING_POSITION = 250

def init():
    t.pensize(0)
    t.color(pen_c)
    t.fillcolor(fill_c)

    t.up()
    t.goto(0, STARTING_POSITION)

def draw_circle(num):

    radius = STARTING_SIZE + (num * 20)     # Radius increases by 20 for each new circle
    t.goto(0, t.ycor() - (radius * 2))      # Goes to starting position so there is no overlap with other circles
    
    t.down()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.up()


def main():
    init()
    draw_circle(0)
    draw_circle(1)
    draw_circle(2)
    t.done()

main()