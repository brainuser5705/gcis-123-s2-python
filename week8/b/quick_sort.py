import arrays
import arrays_util

def quick_sort(comparator, an_array):
    if len(an_array) <=1: 
        return an_array
    else: 
        pivot = an_array[0]
        less, same, more = partition(pivot, an_array)
        sorted_less = quick_sort(comparator, less)
        sorted_more = quick_sort(comparator, more)

        sorted_less_same= arrays_util.array_cat(sorted_less, same)
        sorted_array = arrays_util.array_cat(sorted_less_same, sorted_more)

        return sorted_array

def partition(pivot, an_array):

    count_less = 0
    count_same = 0
    count_more = 0

    for index in range(len(an_array)):
    
        if an_array[index] < pivot:
            count_less +=1
        
        if an_array[index] == pivot:
            count_same += 1
        
        if an_array[index] > pivot:
            count_more +=1

    less = arrays.Array(count_less)
    same = arrays.Array(count_same)
    more = arrays.Array(count_more)

    count_less = 0
    count_same = 0
    count_more = 0
    
    for index in range(len(an_array)):
        if an_array[index] < pivot:
            less[count_less] = an_array[index]
            count_less +=1
        if an_array[index] == pivot:
            same[count_same] = an_array[index]
            count_same +=1 
        if an_array[index] > pivot:
            more[count_more] = an_array[index]
            count_more +=1

    return less, same, more