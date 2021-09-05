"""
Guess the turtle output when main() runs
"""

import turtle as t

color = "blue"
radius = 100

def draw_circle(color, num):
    input("Press enter to go to output " + str(num) + "!")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def output1():
    draw_circle(color, 1)

def output2():
    color = "red"
    draw_circle(color, 2)

def output3():
    draw_circle(color, 3)

def output4():
    global color
    color = "green"
    draw_circle(color, 4)

def output5():
    draw_circle(color, 5)

def output6(color):
    color = "orange"
    draw_circle(color, 6)

def output7():
    draw_circle(color, 7)


def main():

    output1()
    
    output2()

    output3()

    output4()

    output5()

    output6(color)

    output7()

    draw_circle(color)

    t.done()

main()
    




    

