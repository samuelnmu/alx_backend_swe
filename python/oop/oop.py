class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return(f"Your name is {self.name} and you are {self.age} years old")
    
person1 = person("Samuel", 24)
print(person1)