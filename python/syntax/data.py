value = input("Enter your data: ")

match value:
    case str():
        print(value, "Is a String")
    case int():
        print(value, "Is an Integer")
    case _:
        print("Invalid input!")