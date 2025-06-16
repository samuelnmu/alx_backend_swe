#Shopping System
class Register():
    def __init__(self, name = "", email = "", password = "", phone = 0):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        
        
    def collect_name(self):
        while True:
            name = input("Enter name: ")
            if name.replace(" ","").isalpha():
                self.name = name
                print("Name saved successfully")
                break
            print("Invalid name! Please use only letters.")
    
    def collect_email(self):
        while True:
            email = input("Enter Email: ")
            if "@" in email and ".":
                self.email = email
                print("Email saved successfully")
                break
            print("Invalid Email, please include @ and .")
    
    def collect_password(self):
        while True:
            password = input("Input password: ")
            if len(password) < 8:
                print("Your password is too short: 8 char minimum!")
                break
            else:
                print("Password saved")
                
            
            

            
new_customer = Register()
new_customer.collect_name()
print(f"Customer Name: {new_customer.name}")

customer_email = Register()
customer_email.collect_email()
print(f"Your email is {customer_email.email}")

new_password = Register()
new_password.collect_password()
print(f"Your password is {new_password.password}")

