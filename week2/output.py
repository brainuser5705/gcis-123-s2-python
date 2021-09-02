"""
What would each variable be equal to after the program runs?

Note that you will need to debug some.
"""

a = 3 + 6 * 5 - 11
b = 6 % 5 / 4
c = 6 % 5 // 4
d = a * 2
#e = 34 // 0 # why is this commented out?
f = "Hello " + " world"
g = str(float("7.0") * int(2.0))
h = "1 " + '1'
i = "1" - "1" # i should be an integer type, why should you change?
j = f + a # what is missing?
k = str("hello") + str(5)
l = k * 2


# i know...this is the worst print statement you have ever seen
print(
    "a: " + str(a) + " " + str(type(a)),
    "b: " + str(b) + " " + str(type(b)),
    "c: " + str(c) + " " + str(type(c)),
    "d: " + str(d) + " " + str(type(d)),
    #"e: " + e + " " + str(type(e)),
    "f: " + str(f) + " " + str(type(f)),
    "g: " + str(g) + " " + str(type(g)),
    "h: " + str(h) + " " + str(type(h)),
    "i: " + str(i) + " " + str(type(i)),
    "j: " + str(j) + " " + str(type(j)),
    "k: " + str(k) + " " + str(type(k)),
    "l: " + str(l) + " " + str(type(l)),
    sep="\n"
)