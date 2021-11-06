import arrays
from arrays_util import swap


def insertion_sort(comparator, array):

    for index in range(0, len(array)-1):

        i = index

        while i >= 0 and not comparator(array[i], array[i+1]):
            swap(array, i, i + 1)
            i -=1

    return array