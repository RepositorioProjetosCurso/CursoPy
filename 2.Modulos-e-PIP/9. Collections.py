from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
frutas = ["Maçã", "Banana", "Abacaxi", "Pêra", "Uva", "Laranja", "Tangerina", "Tamarindo", "Banana", "Laranja", "Uva", "Abacaxi", "Banana"]
print(frutas)
print(Counter(frutas))

print()

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 2025", 157.90, 8.5)
g2 = game("Slitherio", 75, 5.7)
g3 = game("Red Dead Redemption", 300, 10)

print(g1)
print(g2)
print(g3)

print()

# 3 - Ordenando Dicts
students = {"Pedro": 23, "Joana": 19, "Claúdio": 30, "Jonas": 21}
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

print()

# 4 - Utilizando uma fila com ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.pop()
print(deq)

print()