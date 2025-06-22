class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
        
    @classmethod
    def counter(cls):
        return f"Person: {cls.count}"
    
Person1 = Person("Alice")
Person2 = Person("Sam")

print(Person.counter())