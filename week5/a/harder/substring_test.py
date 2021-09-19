from substring import check_substring

def test_substring_a_apple():
    assert check_substring('a','apple') == True

def test_substring_apple_apple():
    assert check_substring('apple','apple') == True

def test_substring_ab_apple():
    assert check_substring('ab','apple') == False

def test_substring_empty_apple():
    assert check_substring('','apple') == True

def test_substring_empty_apple():
    assert check_substring('apples','apple') == False