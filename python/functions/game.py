def user():
    #Collecting users info and storing them in variables
    name = input("Enter name: ")
    age = int(input("Enter your age: "))
    
    #A function that greet's the user and is only called when user is 18+
    def greeting():
            print(f"Hello, {name}! Welcome")
            
    #conditional statement that checks if the user is an adult 
    if age < 18:
        print("You should be in school!")
    else:
        email = input("Enter your email: ")
        gender = input("Enter your Gender(M/F): ")
        greeting()
        
user()
