class Register():
    def __init__(self, name="", email="", password="", phone=""):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
            
    def collect_name(self):
        while True:
            name = input("Enter name: ")
            if name.replace(" ", "").isalpha():
                self.name = name
                print("Name saved successfully")
                break
            print("Invalid name! Please use only letters.")
    
    def collect_email(self):
        while True:
            email = input("Enter Email: ")
            if "@" in email and "." in email:
                self.email = email
                print("Email saved successfully")
                break
            print("Invalid Email, please include @ and .")
    
    def collect_password(self):
        while True:
            password = input("Input password: ")
            if len(password) < 8:
                print("Your password is too short: 8 char minimum!")
            else:
                self.password = password
                print("Password saved")
                break

    def collect_phone(self):
        while True:
            phone = input("Enter Phone number: ")
            if not phone.isdigit():
                print("Phone number should contain only digits!")
            elif len(phone) < 10:
                print("Invalid phone number! Must be at least 10 digits.")
            else:
                self.phone = phone
                print("Phone number saved.")
                break


# Using only one instance instead of 4
new_customer = Register()
new_customer.collect_name()
new_customer.collect_email()
new_customer.collect_password()
new_customer.collect_phone()

print("\n=== Registration Summary ===")
print(f"Customer Name: {new_customer.name}")
print(f"Email: {new_customer.email}")
print(f"Password: {new_customer.password}")
print(f"Phone: {new_customer.phone}")
