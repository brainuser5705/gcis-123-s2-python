from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

import compare

import arrays
import random

LEN = 10
SEED = 5

def get_algorithm(num):
    if num == 1:
        return insertion_sort
    elif num == 2:
        return merge_sort
    elif num == 3:
        return quick_sort
    else:
        return None

def get_comparator(num):
    if num == 1:
        return compare.increasing
    elif num == 2:
        return compare.decreasing
    else:
        return None

def generate_random_array(length, seed):
    # TO DO:
    arr = arrays.Array(length)
    random.seed(seed)
    for i in range(length):
        arr[i] = random.randint(0,100)
    return arr
    
def main():

    print("sorting program")

    algo = None
    while (algo == None):
        algo_input = int(input("What algorithm? "))
        algo = get_algorithm(algo_input)

    comparator = None
    while (comparator == None):
        comparator_input = int(input("What comparator? "))
        comparator = get_comparator(comparator_input)

    arr = generate_random_array(LEN, SEED)
    sorted_arr = algo(comparator, arr)
    print(sorted_arr)

if __name__ == '__main__':
    main()