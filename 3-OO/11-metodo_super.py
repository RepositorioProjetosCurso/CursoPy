class Phone:
    def __init__(self, brand, modelName, price):
        self._brand = brand
        self._modelName = modelName
        self._price = price
    
    def __str__(self):
        return f"{self._brand} {self._modelName}"
    
    @staticmethod
    def makeCall(phone_numb):
        print(f"Calling to {phone_numb}...")
        
class SmartPhone(Phone):
    def __init__(self, brand, modelName, price, ram, backCamera, internalMemory):
        super().__init__(brand, modelName, price)
        
        self.ram = ram
        self.backCamera = backCamera
        self.internalMemory = internalMemory
        
MotoG = Phone("Motorola", "G9", 1000)
print(MotoG)
print()
MotoG.makeCall(986082874)
print(f"The Price of {MotoG._brand} {MotoG._modelName} is USD$ {MotoG._price}")
print(vars(MotoG))
print()

Iphone = SmartPhone("Apple", "Iphone 11", 5000, "4GB", "25MP", "128GB")
print(Iphone)
print()
Iphone.makeCall(986082874)
print(f"The Price of {Iphone._brand} {Iphone._modelName} is USD$ {Iphone._price}")
print(vars(Iphone))