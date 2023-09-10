def reversed(n: int):
    """
    Function takes in an integer and returns the integer with the digits in reversed order.
    """
    assert(type(n) == int)
    return int(str(n)[::-1])

def formatter(n: int):
    """
    Function takes in an integer and returns the integer as a tuple of strings in binary followed by octal.
    """
    return bin(n), oct(n)