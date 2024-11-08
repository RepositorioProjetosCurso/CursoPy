'''
    Não possiblita recuperar valores via fatiamento/slice
'''
gameSet = {"Fifa 25", "Cook in Joy", "Ben 10", "Warzone", "GTA V"}

# Buscar o tamanho do set
print(len(gameSet))

# True e 1 são considerados o mesmo valor
exemplaSet =    {"Fifa 25", True, 1, 98.50}
print(exemplaSet)

# Adicionar item de outro set
gameSet.update(exemplaSet)
print(gameSet)

# Remove um item
gameSet.remove(True)
gameSet.remove(98.50)
print(gameSet)