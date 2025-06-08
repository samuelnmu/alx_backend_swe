
def game():
    secret_number = 4
    guess = int(input("Enter a number: "))

    match guess:
        case _ if guess == secret_number:
            print("🎉 Congratulations, you guessed it!")
        case _ if guess < secret_number:
            print(" Nope, your guess is a bit low.")
            again()
        case _ if guess > secret_number:
            print(" Oops, your guess is a bit high.")
            again()
def again():
    response = input("Wanna try again? (Y/Yes or N/No): ").lower().strip()

    match response:
        case "y" | "yes":
            game()
        case "n" | "no":
            print("See you soon!")
        case _:
            print("Invalid choice.")
            again()

game()
