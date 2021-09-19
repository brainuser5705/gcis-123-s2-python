"""
Returns true if substring is in string, else False
"""

def check_substring(sub, str):
    #return sub in str

    # if substring is longer than the string
    if len(sub) > len(str):
        return False
    
    # if substring is the string
    if sub == str:
        return True

    i = 0
    while i < len(str) - len(sub):

        # check each letter of the sub and compare with the string
        j = 0
        while j < len(sub):
            if sub[j] != str[i+j]:
                break
            j += 1

        # check if the index has reached the end of the substring and
        # did not break out
        if j == len(sub):
            return True

        i += 1
    
    return False
        