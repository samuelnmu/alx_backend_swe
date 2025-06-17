# Import the bcrypt library for password hashing
import bcrypt 

# Define a class for user registration
class Register():
    
    def __init__(self, name="", email="", password="", phone=""):
        # Initialize user attributes
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        
    # Method to collect and validate user's name
    def collect_name(self):
        while True:
            name = input("Enter name: ")
            # Remove spaces and check if all characters are letters
            if name.replace(" ", "").isalpha():
                self.name = name
                print("Name saved successfully! ")
                break
            else:
                print("Enter a valid name!")   
    
    # Method to collect and validate user's email
    def collect_email(self):
        while True:
            email = input("Enter Email: ")
            # Basic validation: check for '@' and '.'
            if "@" in email and "." in email:
                self.email = email
                print("Email saved!")
                break
            else:
                print("Email must contain '@' and '.'")
    
    # Method to collect and hash user's password
    def collect_password(self):
        while True:
            try:
                password = input("Enter password: ")
                if len(password) < 8:
                    print("Password too short — 8 characters minimum")
                else:
                    # Hash the password using bcrypt
                    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
                    # Decode hash to store as a string
                    self.password = hashed.decode("utf-8")
                    print("Password is saved!")
                    break
            except ValueError as e:
                print("An error occurred:", e)
            
    # Method to collect and validate user's phone number
    def collect_phone(self):
        while True:
            phone = input("Enter Phone Number: ")
            # Check if input is numeric and has at least 10 digits
            if not phone.isdigit() or len(phone) < 10:
                print("Invalid phone number")
            else:
                self.phone = phone
                print("Phone number saved!")
                break

# Create a new Register object for a customer
new_customer = Register()

# Collect user information
new_customer.collect_name()
new_customer.collect_email()
new_customer.collect_phone()
new_customer.collect_password()

# Display registration summary (password hidden for security)
print("\n=== Registration Summary ===")
print(f"Customer Name: {new_customer.name}")
print(f"Email: {new_customer.email}")
print(f"Phone: {new_customer.phone}")
print(f"Hashed Password: {new_customer.password}")
