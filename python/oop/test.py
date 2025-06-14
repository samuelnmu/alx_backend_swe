try:
    with open("file.txt") as f:
        print("File opened successfully")
        print("file content")
        print(f.read())
except FileNotFoundError:
    print("The above file does not exist!")
except IOError as e:
    print(f"Error reading file {e}")