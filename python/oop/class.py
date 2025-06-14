class  Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        
    def speak(self):
        pass
    
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} Meows as he {self.action}"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} Barks as he {self.action}"
    
#polymorphism
zoo = [
    Cat("Nice", "Jumps"),
    Dog("Bosco","Runs")
]

for animal in zoo:
    print(animal.speak())