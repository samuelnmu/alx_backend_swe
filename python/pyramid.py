rows = 5
row = 1

while row <= rows:
    # Print spaces
    space = 1
    while space <= (rows - row):
        print(" ", end="")
        space += 1

    # Print asterisks
    star = 1
    while star <= (2 * row - 1):
        print("*", end="")
        star += 1

    print()  # Move to the next line
    row += 1
