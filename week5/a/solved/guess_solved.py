from random import randint

def check_guess(guess, answer):
    return guess == answer

def main():
    answer = randint(1,10)
    
    guess = None
    i = 1
    while not check_guess(guess, answer):
        guess = int(input("guess " + str(i) + ":"))
        i += 1
        
    print("You guessed it!")

if __name__ == '__main__':
    main()