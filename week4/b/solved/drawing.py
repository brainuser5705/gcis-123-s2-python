import turtle as t
from random import randint
from math import sqrt

WIDTH_BOUNDS = 100
HEIGHT_BOUNDS = 100
PI = 3.14

def goto_random():
    random_x = randint(-WIDTH_BOUNDS,WIDTH_BOUNDS)
    random_y = randint(-HEIGHT_BOUNDS,HEIGHT_BOUNDS)
    t.up()
    t.goto(random_x, random_y)
    t.down()

def circle(rad):
    t.circle(rad)
    return PI * rad**2

def triangle(len):
    t.left(120) # orient
    t.fd(len)
    t.left(120)
    t.fd(len)
    t.left(120)
    t.fd(len)

    height = sqrt(len**2 -(len/2)**2) 
    return (len * height) / 2

def rectangle(len, wid):
    t.fd(len)
    t.left(90)
    t.fd(wid)
    t.left(90)
    t.fd(len)
    t.left(90)
    t.fd(wid)
    t.left(90) # reorient

    return len * wid

    
def main():
    goto_random()
    circle_area = circle(100)
    goto_random()
    triangle_area = triangle(20)
    goto_random()
    rectangle_area = rectangle(30, 40)

    print("Circle Area:", circle_area)
    print("Triangle Area:", triangle_area)
    print("Rectangle Area:", rectangle_area)
    print("Total Area:", circle_area + triangle_area + rectangle_area)


# if __name__ == '__main__':
#     main()

main()



