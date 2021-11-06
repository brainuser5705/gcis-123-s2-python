import arrays
import random
import time

def is_dup(num, array, size):
    for i in range(size):
        if(num == array[i]):
            return True
    return False

def main():
    user_input = int(input("Enter an array length: "))
    an_array = arrays.Array(user_input)
    random.seed(5)
    begin = time.perf_counter()
    for i in range(len(an_array)):
        rand_num = random.randint(1,user_input)
        while(is_dup(rand_num, an_array, i)):
            rand_num = random.randint(1,user_input)
        an_array[i] = rand_num
    end = time.perf_counter()

    el = end - begin
    print(el)
    print(an_array)


if __name__ == "__main__":
    main()

   

