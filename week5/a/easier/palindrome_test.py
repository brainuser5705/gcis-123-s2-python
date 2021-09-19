from palindrome import is_palindrome

"""
Odd length strings
"""
def test_aba():
    assert is_palindrome('aba') == True

def test_abc():
    assert is_palindrome('abc') == False

def test_tacocat():
    assert is_palindrome('tacocat') == True

"""
Even length strings
"""
def test_abba():
    assert is_palindrome('abba') == True

def test_abbc():
    assert is_palindrome('abbc') == False

def test_mommom():
    assert is_palindrome('mommom') == True

"""
Edge cases
"""
def test_empty():
    assert is_palindrome('') == True

def test_numbers():
    assert is_palindrome('1234321') == True