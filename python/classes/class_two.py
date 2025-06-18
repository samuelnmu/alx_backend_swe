class Library:
    # Constructor method: initializes the Library instance
    def __init__(self, file="books.txt"):
        self.file = file  # Store the filename for saving/loading books
        self.books = self.load_book()  # Load existing books from file

    # Method to load books from the file
    def load_book(self):
        try:
            # Try to open the file in read mode
            with open(self.file, "r") as f:
                # Read all lines and remove newline characters, returning a list
                return f.read().splitlines()
        except FileNotFoundError:
            # If file doesn't exist, return an empty list
            return []

    # Method to add books to the list and file
    def add_books(self):
        while True:
            # Ask user to input a book title or type 'exit' to stop
            user = input("Add book: or enter 'exit' to quit: ")
            if user.lower() == "exit":
                break  # Exit the loop if user types 'exit'
            self.books.append(user)  # Add book to the internal list
            with open(self.file, "a") as f:
                f.write(user + "\n")  # Append book to the file with newline

    # Method to return a string representation of the book list
    def __str__(self):
        # Join all book titles with spaces and return a message
        return f"Available books are: {' '.join(self.books)}"

# Create an instance of the Library class
my_library = Library()

# Start adding books through user input
my_library.add_books()

# Print out the list of available books
print(my_library)
