name = str(input("Enter name: "))
age = int(input("Enter age: "))

match age:
    case 18 | 19:
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are too young!")
    case _:
        print("Invalid!")