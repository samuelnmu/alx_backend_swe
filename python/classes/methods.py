class Filehandle:
    def __init__(self, file = "books.txt"):
        self.file = file
        
    def read_file (self):
        with open(self.file, "r") as f:
            return f.read()
        
    def __str__(self):
        return self.file
    
            
file = Filehandle()
print(file.read_file())
            