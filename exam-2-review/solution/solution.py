import re

WORD_ARR = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def read_numbers(filename): 
    arr = []
    with open(filename) as file:
        for line in file:
            if len(re.findall("\d{2}", line)) != 0 and int(line) >= 0:
                arr.append(int(line))
    return arr

def _swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def insertion_sort(array):

    for index in range(0, len(array)-1):

        i = index

        while i >= 0 and array[i] > array[i+1]:
            _swap(array, i, i + 1)
            i -=1

def convert(word, num):
    if (word == "" and num == 0):
        return "zero"
    elif (num == 0):
        return word
    else:
        last_digit = num % 10 # can be used as index to get word

        # updating for the next recursive stack
        new_word = WORD_ARR[last_digit] + " " + word
        new_num = num // 10

        return convert(new_word, new_num)
            
def main():
    arr = read_numbers("numbers.txt")
    insertion_sort(arr)

    for num in arr:
        print(convert("", num))

if __name__ == '__main__':
    main()