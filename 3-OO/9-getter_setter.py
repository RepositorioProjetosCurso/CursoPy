class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Name: {self.name} - Salary: {self.__salary}")
        
    # Método para buscar dados
    def get_salary(self):
        return self.__salary
    
    # Método para modificar o atributo privado
    def set_salary(self, salary):
        self.__salary = salary
        
fulano = Employee("João Pedro", 4250)
sicrano = Employee("Julia Carosella", 3750)

fulano.show()
print()

fulano.set_salary(45000)
fulano.show()