from decoratorTeste import my_decorator, uppercase_decorator, split_string

# Exemplo 01
@my_decorator
def my_function():
    print("Dentro da função")
    
my_function()

# Exemplo 02
@uppercase_decorator
def text():
    return "Hello World"

print(text())

# Exemplo 03
@split_string
@uppercase_decorator
def exemple():
    return "Aprendendo python e criando decorators"

print(exemple())