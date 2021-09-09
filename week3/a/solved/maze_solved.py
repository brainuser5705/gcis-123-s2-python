import turtle as t

image_name = "maze.gif"
SIZE = 25

def init():

    # import the maze image
    screen = t.Screen()
    screen.setup(800,800)
    screen.bgpic(image_name)

    # move turtle to starting position
    t.up()
    t.goto(0, -250)
    t.setheading(90)

    t.down()
    t.fd(200)
    t.left(90)

def draw_P(xextra_t, xextra_b, yextra):
    t.forward(SIZE * (2 + xextra_t))
    t.right(90)
    t.fd(SIZE * (1 + yextra))
    t.left(90)
    t.fd(SIZE * 3)
    t.left(90)
    t.fd(SIZE * (4 + yextra))
    t.left(90)
    t.fd(SIZE * (3 + yextra))
    t.left(90)
    t.fd(SIZE)
    t.left(90)
    t.fd(SIZE * (2 + xextra_b))
    t.right(90)
    t.fd(SIZE * (2 + yextra))
    t.right(90)
    t.fd(SIZE)
    t.right(90)
    t.fd(SIZE * (1 + yextra))
    t.left(90)
    t.fd(SIZE * (2 + xextra_b))
    t.right(90)
    t.fd(SIZE * 3)
    t.right(90)

def transition():
    t.fd(SIZE * 9)
    t.right(90)
    t.fd(SIZE * 10)
    t.right(90)
    t.fd(200)
    t.left(90)

def main():

    init()
    
    draw_P(0,0,0)
    draw_P(3,4,4)
    transition()

    draw_P(0,0,0)
    draw_P(3,4,4)
    transition()

    t.fd(SIZE)

    draw_P(0,0,0)
    draw_P(3,4,4)
    transition()

    draw_P(0,0,0)
    draw_P(3,4,4)
    transition()

    t.right(90)
    t.fd(SIZE)

    t.done()

main()
