class Animal():
    name =  ""
    size = 0
    color = ""
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    race = ""
    
    def scape(self):
        print(f"{self.name} is scaping")
        
class Horse(Animal):
    race = ""
    
    def gallop(self):
        print(f"{self.name} is galloping")
        
class Lion(Animal):
    mane = True
    
    def hunt(self):
        print(f"{self.name} is hunting")
        
h = Horse()
h.name = "Rex"
h.color = "Black"
h.eat()
h.gallop()
print()

l = Lion()
l.name = "Simba"
l.color = "Yellow"
l.eat()
l.hunt()
print()

d = Dog()
d.name = "Duddy"
d.color = "Gray"
d.eat()
d.scape()