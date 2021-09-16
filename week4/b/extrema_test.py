from extrema import get_max, get_min

####### get_min() tests #########

def test_min_3_4():
    assert get_min(3,4) == 3

def test_min_10_2():
    assert get_min(10,2) == 2

def test_min_0_neg1():
    assert get_min(0,-1) == -1 

def test_min_9_9():
    assert get_min(9,9) == 9


####### get_max() tests #########

def test_max_3_4():
    assert get_max(3,4) == 4

def test_max_10_2():
    assert get_max(10,2) == 10

def test_max_0_neg1():
    assert get_max(0,-1) == 0 

def test_max_9_9():
    assert get_max(9,9) == 9
