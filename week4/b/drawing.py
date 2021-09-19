from math import sqrt, pi
def rectangle(length,width):

    if length>0 and width>0:
        area = length*width
        return area
    return None

def triangle(side):
    if side>0:
        height=sqrt(side**2-(side/2)**2)
        area=.5*side*height
        return area
    return None

def circle(radius):
    if radius >0:
        area = pi*radius**2
        return area
    return None

def main():
    rectangle(1,2)

if __name__ == '__main__':
    main()