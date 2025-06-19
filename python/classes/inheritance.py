class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Make a sound: "
    
    def behaviour(self):
        return f"The above animal you have selected is a {self.name}, and it {self.sound()}"
    
            
    
class Cat(Animal):
    
    def sound(self):
        return "meows"
    

class Dog(Animal):
    
    def sound(self):
        return "Barks"
    

animal_type =input("Choose animal: ").lower().strip()

if animal_type == "cat":
    animal = Cat("cat")
elif animal_type == "dog":
    animal = Dog("dog")
else:
    print("We dont have the above animal!")
    exit()

print(animal.behaviour())
    