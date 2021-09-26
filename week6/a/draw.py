import turtle as t
import words # validate_string, is_palindrome, is_vowel, get_vowel_count

SIZE = 20
ROWS = 20
COLS = 20

def init():
    """
    Initializes the turtle at the top left corner of the grid
    """
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
    pass

def draw_column(string):
    """
    Draw the string as a column of letter pixels
    :param: string - the string to draw
    """
    pass

def main():
    """
    Main function to draw and color the words.
    """
    init()
    # TO DO: Write the rest of the main function

if __name__ == '__main__':
    main()


