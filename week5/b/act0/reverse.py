"""
Reverse a string with a for loop and print it.
"""

def reverse(string):
    str = ""
    for x in range (-1, -len(string) - 1, -1):
        str += string[x]

    return str

def main():
    print(reverse('newyork'))

main()