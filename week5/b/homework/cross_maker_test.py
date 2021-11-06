import turtle as t

PIXEL_SIZE = 25
ROWS = 20
COLS = 20

START_X = -(COLS/2)*PIXEL_SIZE
START_Y = (ROWS/2)*PIXEL_SIZE

def init():
    t.speed(0)

    t.up()
    t.goto(START_X, START_Y)
    t.down()

def draw_letter_box(color, letter):

    # Draws the square
    t.fillcolor(color)
    t.begin_fill()
    i = 0
    while i < 4:
        t.fd(PIXEL_SIZE)
        t.left(90)
        i += 1
    t.end_fill()

    # Writes the letter in the center of the square
    t.fd(PIXEL_SIZE/2)
    t.write(letter, align='center', font=("Arial", 19, "normal"))
    t.bk(PIXEL_SIZE/2)

def write_word(x, y, word, is_horizontal):
    if (validate_string(word, x, y, is_horizontal)):
        
        t.up()
        t.goto(START_X + (x*PIXEL_SIZE), START_Y - (y*PIXEL_SIZE))
        t.down()

        i = 0
        while i < len(word):
            draw_letter_box('red', word[i])

            # transition to next letter
            if is_horizontal:
                t.fd(PIXEL_SIZE)
            else:
                t.up()
                t.goto(t.xcor(), t.ycor()-PIXEL_SIZE)
                t.down()

            i += 1

def validate_string(word, x, y, is_horizontal):
    strlen = len(word)
    if is_horizontal:
        return x + strlen <= ROWS
    else:
        # -y because the starting row is in the positive region
        return y + strlen <= COLS
    
def ask_user():
    while True:
        command = input("What word: ")

        # exit out of loop is no input given
        if command == '':
            break

        properties = command.split(' ')
        x = int(properties[0])
        y = int(properties[1])
        word = properties[2]
        
        if (properties[3] == 'h'):
            is_horizontal = True
        elif (properties[3] == 'v'):
            is_horizontal = False

        write_word(x, y, word, is_horizontal)


def main():
    init()
    ask_user()
    t.done()

if __name__ == '__main__':
    main()
