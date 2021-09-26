def validate_string(string):
    """
    Checks if a string contains alphabetic characters. Note that an empty string is valid.
    :param: string - the string to check
    :returns: True - if string is alphabetic, False - otherwise
    """
    return string.isalpha()
    
def is_vowel(character):
    """
    Checks if a character is a vowel
    :param: character - an alphabetic character
    :returns: True - if vowel, False - otherwise
    """
    return character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'


def get_vowel_count(string):
    """
    Gets the number of vowels in the string.
    :returns: number of vowels in the string
    """
    counter = 0
    for i in range(len(string)):
        if is_vowel(string[i]):
            counter += 1

    return counter
