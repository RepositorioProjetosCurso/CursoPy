class Animal():
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Fish(Animal):
    race = ""
                
class Parrots(Animal):
    color = ""
    
class Zoo:
    def __init__(self):
        self.animals.dict = {}