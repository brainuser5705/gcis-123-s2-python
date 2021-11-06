import solution

def test_read_numbers():
    arr = solution.read_numbers("test/test_numbers.txt")
    assert arr == [100, 23, 60]

def test_convert():
    # setup
    word = ""
    num = 10

    # invoke
    new_word = solution.convert(word, num)

    # analyze 
    assert new_word == "one zero "