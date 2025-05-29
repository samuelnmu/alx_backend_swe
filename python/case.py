day = input("Enter day: ").lower()

match day:
    case "monday":
        print("start of the week")
    case "tuesday":
        print("Yaaay")
    case "wednesday":
        print("Weekend is almost")
    case "thursday":
        print("TBT innit")
    case "friday":
        print("Itss friiiiiiiday")
    case "satarday":
        team = input("Which team are you supporting? ")
        print(team, "Is a big one indeed!")
    case "sunday":
        print("Lets go to Church")
    case _:
        print("Invalid input")