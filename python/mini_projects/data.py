import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   second_name TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   phone INTEGER
               )
               """)
conn.commit()

class Credentials:
    
    def __init__(self, first_name = "", second_name = "", email = "",phone = 0):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.phone = phone
        
    
    def collect_data(self):   
        try:
            self.first_name = input("Enter first name: ")
            self.second_name = input("Enter second name: ")
            self.email = input("Enter Email: ")
            self.phone = int(input("Enter Phone number: "))
        except ValueError as e:
            return f"Invalid Values {e}"
        
    def insert_data(self):
        try:
            cursor.execute("""
                           INSERT INTO users(first_name, second_name, email, phone)
                           VALUES(?,?,?,?)
                           """,(self.first_name, self.second_name, self.email, self.phone))
            conn.commit()
            print("User Data Saved!")
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}") 
            
    def show_users(self):
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        if users:
            print("\n ****Registered Users***")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[3]}, Phone: {user[4]}")
        else:
            print("No Users found!")
            
    def export_users_to_txt(self, filename="users.txt"):
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        if not users:
            print("No users to export.")
            return

        with open(filename, "w") as file:
            file.write("ID | First Name | Second Name | Email | Phone\n")
            file.write("-" * 50 + "\n")
            for user in users:
                file.write(f"{user[0]} | {user[1]} | {user[2]} | {user[3]} | {user[4]}\n")

        print(f"✅ Users exported successfully to {filename}")

         
# user = Credentials()
# user.collect_data()
# user.insert_data()

# users = Credentials()
# users.show_users()

user = Credentials()
user.export_users_to_txt()


conn.close()
    
    