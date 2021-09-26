import turtle as t
import words_solved # validate_string, is_palindrome, is_vowel, get_vowel_count

SIZE = 25
ROWS = 20
COLS = 20

def init():
    """
    Initializes the turtle at the top left corner of the grid
    """
    t.speed(0)

    start_x = -(COLS/2) * SIZE
    start_y = (ROWS/2) * SIZE
    t.up()
    t.goto(start_x, start_y)
    t.down()

def draw_letter_pixel(color, letter):
    """
    Draws a pixel of given color with the letter in the center.
    :param: color - the color of the pixel
    :param: letter - the letter to put in the center of the pixel
    """
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.fd(SIZE)
        t.left(90)

    t.end_fill()

    # draw the letter in the center
    t.fd(SIZE/2)
    t.write(letter, align='center', font=("Arial", 19, "normal"))
    t.bk(SIZE/2)


def draw_string(string):
    """
    Draw the string as a column of letter pixels and gets the number of vowels
    :param: string - the string to draw
    :returns: num_vowels - the number of vowel in the string
    """
    i = 0
    while i < len(string):

        char = string[i]

        if (words_solved.is_vowel(string[i])):
            color = "red"
        else:
            color = "white"

        draw_letter_pixel(color, char)

        # set turtle to position to draw next letter
        transition_next_letter()

        i += 1

    return words_solved.get_vowel_count(string)

def transition_next_letter():
    """
    Helper function to set turtle to correct position to draw next letter
    in the column
    """
    t.up()
    t.seth(270)
    t.fd(SIZE)
    t.seth(0)
    t.down()

def next_column():
    """
    Moves the turtle to the start of the next column
    """
    t.up()
    t.goto(t.xcor() + SIZE, (ROWS/2) * SIZE)
    t.down()

def main():
    """
    Main function to get user input and draw the words.
    """
    init()

    # TO DO: Write the rest of the main function
    input_count = 0
    while input_count < COLS:

        word = input("What word: ")

        # program ends on empty string input
        if word == "":
            break

        vowels = draw_string(word)
        print("Number of vowels in", word + ":", vowels)
        next_column()

        input_count += 1

    t.done()


if __name__ == '__main__':
    main()


