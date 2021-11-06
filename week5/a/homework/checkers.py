import turtle as t

PIXEL_SIZE = 20
ROWS = 20
COLS = 20

def init():
    """
    Initializes the turtle by putting it in the top left corner of the grid
    """
    t.speed(0)

    t.up()
    t.goto(-(COLS*PIXEL_SIZE)/2, (ROWS*PIXEL_SIZE)/2)
    t.down()

def draw_pixel(color):
    """
    Draws a pixel of specified color
    @param color        a string representing the color of the pixel
    @uses PIXEL_SIZE    the dimension of the pixel
    """
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(PIXEL_SIZE)
        t.left(90)
    t.end_fill()
    
def draw_alternating_row(start_color, other_color):
    """
    Draws a row of pixels with alternating colors
    @param start_color      the color of the first pixel in the row
    @param other_color      the other color to alternate with
    @uses PIXEL_SIZE        to transition to the next pixel
    """

    i = 0
    while i < COLS/2:
        # draws two pixels in one loop, that is it only loops COLS/2 times
        draw_pixel(start_color)
        t.fd(PIXEL_SIZE)
        draw_pixel(other_color)
        t.fd(PIXEL_SIZE)
        i += 1

def next_row():
    """
    Moves the turtle to the start of the next row
    @pre turtle is at the end of the row
    """
    t.up()
    t.goto(-(COLS/2)*PIXEL_SIZE, t.ycor()-PIXEL_SIZE)
    t.down()

def draw_checkers():
    """
    Draws the entire 20x20 checker board
    """
    start_red = True

    i = 0
    while i < ROWS:

        if start_red:
            start_color = 'red'
            end_color = 'black'
        else:
            start_color = 'black'
            end_color = 'red'

        draw_alternating_row(start_color, end_color) # interesting scope here
        next_row()

        start_red = not start_red
        i += 1
        

def main():
    init()
    draw_checkers()
    t.done()

if __name__ == '__main__':
    main()


    