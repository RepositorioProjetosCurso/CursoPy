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
        self.animals_dict = {}  # Dicionário para armazenar animais
        
    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category  # Mapeia o nome do animal para o objeto
        
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():  # Itera pelos objetos armazenados no dicionário
            if animal == category:
                result += 1
        return f"Em nosso Zoologico temos {result} quantidade de {category}"
    

zoo = Zoo()
peixe = Fish("Peixe Palhaço", "Peixes")
papagaio = Parrots("Arara Azul", "Aves")

zoo.add_animal(peixe)
zoo.add_animal(papagaio)

print(zoo.total_of_category("Aves"))  # Deve imprimir: Em nosso Zoologico temos 1 quantidade de Aves
print(zoo.total_of_category("Peixes"))  # Deve imprimir: Em nosso Zoologico temos 1 quantidade de Peixes