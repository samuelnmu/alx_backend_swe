class Birds:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        return f"A {self.name} {self.sound}"
    
class Duck(Birds):
    def __init__(self):
        super().__init__("Duck", "Quacks")
        
obj = Duck().make_sound()
print(obj)