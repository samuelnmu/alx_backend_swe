class Library:
    def __init__(self, filename = "books.txt"):
        self.filename = filename
        self.books = []
    
    def load_books(self):
        try:
            with open(self.books, "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []
    
    def add_books(self):
        while True:
            user = input("Add book or type 'exit' to stop: ")
            if user.lower() == "exit":
                break
            self.books.append(user)
            with open (self.filename, "a") as f:
                f.write(user + "\n")
                
    def __str__(self):
        return f"The available books are: {', '.join(self.books)}"    
my_library = Library()
my_library.add_books()
print(my_library)
