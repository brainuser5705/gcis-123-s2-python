import turtle as t

PIXEL_SIZE = 20
ROWS = 20
COLS = 20

def init():
    t.speed(0)

    t.up()
    t.goto(-(COLS/2)*PIXEL_SIZE, (ROWS/2)*PIXEL_SIZE)
    t.down()

def get_color(char):
    if char == '0':
        color = 'black'
    elif char == '1':
        color = 'white'
    elif char == '2':
        color = 'red'
    elif char == '3':
        color = 'yellow'
    elif char == '4':
        color = 'orange'
    elif char == '5':
        color = 'green'
    elif char == '6':
        color = 'yellowgreen'
    elif char == '7':
        color = 'sienna'
    elif char == '8':
        color = 'tan'
    elif char == '9':
        color = 'gray'
    elif char == 'A':
        color = 'darkgray'
    else: 
        return False

    return color

def draw_color_pixel(color):
    t.fillcolor(color)

    t.begin_fill()
    side = 1
    while side <= 4:
        t.fd(PIXEL_SIZE)
        t.left(90)
        side += 1
    t.end_fill()


def draw_string(str):
    i = 0
    
    while i < len(str):
        color = get_color(str[i])

        if color == False: # for invalid colors
            return False

        draw_color_pixel(color)

        # transition to next pixel
        t.fd(PIXEL_SIZE)
        i += 1

    return True

def next_row():
    t.up()
    t.goto(-(COLS/2)*PIXEL_SIZE, t.ycor()-PIXEL_SIZE)
    t.down()
    
def get_string():
    while True:
        string = input("enter: ")
        can_draw = draw_string(string)

        if string == '' or not can_draw:
            break

        next_row()

def main():
    init()
    get_string()
    t.done()

if __name__ == '__main__':
    main()
