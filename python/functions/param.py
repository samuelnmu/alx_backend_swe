# def calculate_area(length, width):
#     """Calculates the area of a rectangle."""
#     area = length * width
#     print(area)
# calculate_area(5, 6)

def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 6)
area2 = calculate_area(4, 8)

if area1 > area2:
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")
