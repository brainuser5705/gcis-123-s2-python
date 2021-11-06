from random import randint
from turtle import up, down, goto, circle, speed, done

NUM_CIRCLES = 100
CIRCLE_RADIUS = 20

x_cor = None
y_cor = None

speed(0)

i = NUM_CIRCLES
while i != 0:
    rand_x = randint(-5,5) * 50
    rand_y = randint(-5,5) * 50
    
    if rand_x == x_cor or rand_y == y_cor:
        continue

    x_cor = rand_x
    y_cor = rand_y

    up()
    goto(x_cor, y_cor)
    down()
    circle(CIRCLE_RADIUS)

    i -= 1

done()