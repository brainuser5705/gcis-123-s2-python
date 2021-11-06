import arrays

def split(an_array):
    half1 = arrays.Array((len(an_array)+1)//2) # Why do we need a 1 here?
    half2 = arrays.Array(len(an_array)//2)

    for i in range(len(an_array)):
        if i % 2 == 0: 
            half1[i//2] = an_array[i]
        else:
            half2[i//2] = an_array[i]

    return half1, half2


def merge(comparator, sorted1, sorted2):
    result = arrays.Array(len(sorted1) + len(sorted2))

    i1 = 1
    i2 = 1

    i = 0

    while i1 < len(sorted1) or i2 < len(sorted2):

        if comparator(sorted1[i1], sorted2[i2]):
            result[i] = sorted1[i1] 
            i1 += 1
        else:
            result[i] = sorted2[i2]
            i2 +=1
        i+=1

    while i2 < len(sorted2):
        result[i] = sorted2[i2]
        i += 1
        i2 += 1

    while i1 < len(sorted1):
        result[i] = sorted1[i1]
        i += 1
        i1 += 1

    return result

def merge_sort(comparator, arr):
    if len(arr) <= 2:
        return arr
    else:
        arr1, arr2 = split(arr)
        return merge(comparator, merge_sort(comparator, arr1), merge_sort(comparator, arr2))