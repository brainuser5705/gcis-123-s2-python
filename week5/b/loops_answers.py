
def print_even(num, increment):
    """
    1a. Create a function that prints every even numbers, up to 100

    1b. Now edit the function so that it takes in a number and increment, and returns a sum of all numbers in the loop 
    """
    i = 0
    sum_nums = 0 # 1b implementation
    while (i < num): # previously i < 100
        i += increment # previously i += 2
        #print(i)
        sum_nums += i
    
    return sum_nums


def print_vowels(string):
    """
    2. Create a function that prints the vowels of a string in a single line and returns the number of vowels 

    Example input:
    string = "hello world this is a vowel and stuff, hopefully will contain!!!! some vowels"

    "eooiiaoeauoeuioaioeoe"
    returns: 21
    """
    
    lines = ''

    i = 0
    while(i < len(string)): 
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
            lines += string[i]

        i += 1

    print(lines)
    return len(lines)


def fizzbuzz(n):
    """
    3. Use test driven development to create a function that implements fizzbuzz

    Fizzbuzz:
    - prints FizzBuzz if the modulo of 5 and 7 from a number 
    - prints Fizz if only the modulo of 5 
    - prints Buzz if only the module of 7 
    """
    if n % 5 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"

    


def longest_line():
    """
    4. Create a function that accepts an infinite number of input that prints and keeps track
    of the longest line that was entered (the most characters in a line) until the user
    presses ENTER to quit the program

    Example input:
    >> "Hello"
    Longest line: Hello

    >> "Hey this is Patrick"
    Longest line: Hey this is Patrick

    >> "Hi"
    Longset line: Hi

    >> "supercalifragalisticexpialadocious"
    Longest line: supercalifragalisticexpialadocious

    >> 
    """
    longest = "" # Keeps track of the longest string

    loop = True # many ways for while condition
    while(loop):
        lines = input(">> ")
        length_input = len(lines)
        
        if length_input == 0:
            loop = False 

        elif length_input > len(longest):
            longest = lines

        print("Longest:", longest)


def main():
    sumnums = print_even(10, 2)
    print(sumnums)

    a_string = "hello world this is a vowel and stuff, hopefully will contain!!!! some vowels"
    longest = print_vowels(a_string)
    print(longest)

    fizzbuzz(35)

    longest_line()

if __name__ == "__main__":
    main()