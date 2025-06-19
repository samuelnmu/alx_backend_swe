class Animal():
    def __init__(self, name,sound):
        self.name = name
        self.animal_sound = sound
    
    def kingdom():
        return "Domestic Animal"
        
    def describe(self):
        return f"A {self.name}, {self.animal_sound}"
    
class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "Barks")
        

dog = Dog()
print(dog.describe())

