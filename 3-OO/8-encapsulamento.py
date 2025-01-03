class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Name: {self.name} - Salary: {self.__salary}")
        
fulano = Employee("João Pedro", 4250)
sicrano = Employee("Julia Carosella", 3750)

fulano.show()
sicrano.show()

fulano.__salary = 40000
fulano.show()