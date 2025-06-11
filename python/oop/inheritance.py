#class and objects
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass

#inheritance 
class Dog(Animal):
    def speak(self):
        return f"{self.name} Barks"

#polymorphism
zoo = [
    Dog("Mamba")
]
for animal in zoo:
    print(animal.speak())