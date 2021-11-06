from wc import count_file

def test_text1():
    assert count_file('text/text1.txt') == "lc:3,wc:7,cc:22"  

# TODO: create more test functions for different text files
def test_text2():
    assert count_file('text/text2.txt') == "lc:0,wc:0,cc:0"

def test_text3():
    assert count_file('text/text3.txt') == "lc:1,wc:8,cc:30"