def is_palindrome(str):

    mid = len(str)/2

    i = 0
    while (i < mid):
        if (str[i] != str[len(str)-1-i]): # you can also do str[i-1]
            return False
        i += 1

    return True

