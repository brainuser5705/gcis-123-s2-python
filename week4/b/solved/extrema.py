def get_max(d1, d2):
    """
    Gets the maximum value between two values
    @param d1   the first value to compare
    @param d2   the second value to compare
    """
    
    if (d1 > d2):
        return d1
    else: 
        return d2

    # verbose "Pythonic" way
    return d1 if d1 > d2 else d2


def get_min(d1, d2):
    """
    Gets the minimum value between two values
    @param d1   the first value to compare
    @param d2   the second value to compare
    """
    
    if (d1 < d2):
        return d1
    else: 
        return d2

