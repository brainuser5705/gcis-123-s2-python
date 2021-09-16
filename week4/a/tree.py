import shape as shape
import random as rand

"""
Trunk and leaves color
"""
LEAVES_COLOR = "green"
TRUNK_COLOR = "brown"

"""
Trunk length and width limits
"""
TRUNK_WID_MIN = 50
TRUNK_WID_MAX = 100
TRUNK_LEN_MIN = 100
TRUNK_LEN_MAX = 200

"""
Dimensions for connecting trunks and leaves
"""
EXTEND = 40     # how much do the leaves extend from the edge of the trunk
HIDE = 50       # how much do the leaves extend from the top of the trunk


t = shape.t

def init():
    t.up()
    t.goto(-250,-100)

"""
Helper functions to draw the different parts of the tree.
"""
def trunk():
    len = rand.randint(TRUNK_LEN_MIN, TRUNK_LEN_MAX)
    wid = rand.randint(TRUNK_WID_MIN, TRUNK_WID_MAX)
    shape.draw_rectangle(TRUNK_COLOR, len, wid)
    return wid

# trunk_wid is a parameter because the leaves size is dependent on the trunk's width
def circle_leaves(trunk_wid):
    t.up()
    t.goto(t.xcor()+(trunk_wid/2), t.ycor()-HIDE)
    shape.draw_circle(LEAVES_COLOR, trunk_wid + EXTEND)

def pine_leaves(trunk_wid):
    t.up()
    t.goto(t.xcor()-EXTEND, t.ycor()-HIDE)
    shape.draw_triangle(LEAVES_COLOR, trunk_wid + 2 * EXTEND)

"""
Tree drawing functions
"""
def draw_circle_tree():
    trunk_wid = trunk()
    circle_leaves(trunk_wid)

def draw_pine_tree():
    trunk_wid = trunk()
    pine_leaves(trunk_wid)

   
def main():
    init()
    draw_circle_tree()
    t.up()
    t.goto(200,-100)
    draw_pine_tree()
    t.done()

main()
