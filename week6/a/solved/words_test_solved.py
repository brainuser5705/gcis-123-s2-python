import words

def test_validate_string_true():
    # Set
    string = "abc"

    # invoke
    value = words.validate_string(string)

    # assert
    assert value == True

def test_validate_string_false():
    # Set
    string = "123"

    # invoke
    value = words.validate_string(string)

    # assert
    assert value == False

def test_is_vowel_true():
    # set
    character = 'a'

    # invoke
    value = words.is_vowel(character)

    # assert
    assert value == True

def test_is_vowel_false():
    # set
    character = 'z'

    # invoke
    value = words.is_vowel(character)

    # assert
    assert value == False

def test_get_vowel_count():
    #set 
    string = 'pizza'

    #invoke
    value = words.get_vowel_count(string)

    #assert
    assert value == 2

def test_get_vowel_count_other_word():
    #set 
    string = 'helloi'

    #invoke
    value = words.get_vowel_count(string)

    #assert
    assert value == 3