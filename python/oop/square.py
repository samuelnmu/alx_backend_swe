def square(x):
    """Returns the square of a number"""
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be numeric")
    return x ** 2