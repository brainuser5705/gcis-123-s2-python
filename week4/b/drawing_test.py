"""
Test each drawing function to see if they compute the area correctly.
"""
from math import sqrt, pi
from drawing import rectangle, triangle, circle

def test_rectangle():
    assert rectangle(3,4) == 12

def test_rectangle1():
    assert rectangle(-3,4)==None

def test_rectangle2():
    assert rectangle(-3,-4)==None

# def test_triangle():
#     assert triangle(4)==2*2*sqrt(3)
# def test_triangle1():
#     assert triangle(-4)==None
# def test_circle():
#     assert circle(4)==pi*(4**2)
# def test_circle1():
#     assert circle(-4)==None
