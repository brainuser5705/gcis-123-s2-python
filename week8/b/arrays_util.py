import arrays

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def array_cat(array1, array2):
    len1 = len(array1)
    len2 = len(array2)
    result = arrays.Array(len1+ len2)

    for index in range(len1):
        result[index] = array1[index]

    for index in range(len2):
        result[index + len1] = array2[index]

    return result