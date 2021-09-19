"""
Jin Moon
"""

def fizzbuzz(number):
    """
    Use test driven development to create a function that implements fizzbuzz (in a separate file)

    Fizzbuzz:
    - prints FizzBuzz if the modulo of 3 and 5 from a number has a remainder of 0
    - prints Fizz if only the modulo of 3 has a remainder of 0
    - prints Buzz if only the module of 5 has a remainder of 0
    """

    i = 1
    while i <= number:
        print(str(i) + ": ", end='')
        if i % 3 == 0:
            print("Fizz", end='')
        if i % 5 == 0:
            print("Buzz", end='')

        i += 1
        print('')

def main():
    max = input("What number do you want to go up to: ")
    fizzbuzz(int(max))


if __name__ == '__main__':
    main()