"""
The purpose of this exercise is to practice conditions, variables and loops using turtle!
The end goal would be to draw a polygon flower: https://i.imgur.com/XTwZ4lG.png

Be sure to implement each function incrementally!
"""

import turtle as t

"""
Color constants for mapping to integers. Map # to COLOR_#
"""
COLOR_LESS_THAN_3 = "white"
COLOR_3 = "maroon"
COLOR_4 = "red"
COLOR_5 = "orange"
COLOR_6 = "yellow"
COLOR_7 = "green"
COLOR_8 = "blue"
COLOR_9 = "indigo" 
COLOR_10 = "violet"
COLOR_MORE_THAN_10 = "black"

def initialize(speed, tracer = True):
    """Initialization function

    Args:
        x (int): x coordinate
        y (int): y coordinate
        speed (int): Speed of the turtle
        tracer (boolean): False if the turtle should immediately draw the shapes
    """
    t.goto(-50, -75)
    t.speed(speed)
    t.tracer(tracer)


def get_color (code):
    """ 
    Implement a function that maps and returns an integer to a color (string).
    
    Utilize the color constants that are given in the python file.

    Color codes below 3 should return WHITE
    Color codes above 10 should return BLACK
    """
    
    pass


def draw_polygon (num_sides, length, color):
    """
    The function draws a num_sides polygon where each side length is specified by length with the given fill 
    color. 

    Example: draw_polygon(5, 10, "orange") would draw an orange 5 sided polygon with the perimeter returning 50
    
    Hint: Rotate to the right by 360/num_sides to easily draw any polygon. 

    The function should return the sum (perimeter) of all drawn sides of the polygon 
    """
    
    pass


def draw_poly_circle (num_sides, length, color):
    """ 
    The function draws n-sided  polygons in an n-sided circle where each polygon has a side length of length and a fill 
    color of color.

    After drawing a polygon move forward by half the polygon’s length and turn left by 360/num_sides to draw the circle. 

    Example: draw_poly_circle (7, 50, “blue”) would draw 7 blue septagons which overlap each other in a circular pattern. 

    The function should return the the sum of all perimeters of the polygons drawn.
    """

    pass


def draw_poly_flower (side_length, start_sides, end_sides):
    """
    The function draws polygons from start_sides to end_sides, where each side of a polygon is 
    side_length long. Each polygon circle will use a different color based on the number of sides in the polygon. 
    
    a. start_sides is the number of sides the polygons in the first polygon circle will 
    have.
    b. Each iteration of the polygon circle (poly_circle), will reduce the number of sides
    of the polygon used to draw the circle by one.
    c. Ensure that the polygon will only draw valid shapes throughout each iteration 
    (hint: use end_sides to figure this out!) 

    Example: draw_poly_flower(100, 10, 3) would draw each polygon with sides of 100, starting from a 10 sided polygon
    to 3, with each having different colors based on the color constants
    
    The function should return the total perimeter of all polygons drawn. 
    """
    
    pass


def main ():
    initialize(30)

    ### Use these commented out functions to test your code!
    ###

    #draw_polygon(5,10,"orange")
    #draw_poly_circle(7, 50, "blue")
    #draw_poly_flower(100, 10, 3)


    ### After every function is implemented, update main so that the user takes an input for the length, start_sides and end_sides.
    ### Make sure the perimeter of the poly flower is printed.

    t.done ()

if __name__ == "__main__":
    main ()