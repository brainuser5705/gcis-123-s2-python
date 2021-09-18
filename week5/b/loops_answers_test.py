from loops_answers import fizzbuzz


def test_fb_fizzbuzz():
    # expected
    expected = "FizzBuzz"
    
    # actual
    actual = fizzbuzz(35)
    
    # test
    assert expected == actual

def test_fb_fizz():
    # expected
    expected = "Fizz"

    # actual
    actual = fizzbuzz(10)

    # test
    assert expected == actual


def test_fb_fizz():
    # expected
    expected = "Buzz"

    # actual
    actual = fizzbuzz(14)

    # test
    assert expected == actual