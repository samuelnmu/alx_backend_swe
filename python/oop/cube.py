def cuboid_volume(length):
    """Calculate volume of a cube given its side length"""
    if not isinstance(length, (int, float)):
        raise TypeError("Length must be numeric")
    if length < 0:
        raise ValueError("Length cannot be negative")
    return length ** 3