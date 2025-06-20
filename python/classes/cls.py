class Person:
    count = 0
    
    def __init__(self, peps):
        self.peps = peps
        Person.count +=1
        
    def greet(self):
        return f"Hello {self.peps}"
    
    @classmethod
    def count_person(cls, person_instance):
        return f"The totall is {cls.count}:\n {person_instance.greet()}"
    
person1 = Person("Alice")
person2 = Person("Sam")
person3 = Person("John")

print(Person.count_person(person1))

