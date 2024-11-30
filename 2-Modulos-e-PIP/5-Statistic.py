import statistics

# 1 - Aplicar a média
print(statistics.mean([9, 8 ,5, 4, 7, 3]))

# 2 - Aplicar a mediana
print(statistics.median([9, 8 ,5, 6, 10, 4]))
print(statistics.median([9, 8, 6, 10, 4]))

# 3 - Aplicar a moda
print(statistics.mode([2, 6, 8, 2, 5, 7, 8, 9, 8, 5, 7, 8, 8, 6, 3, 1]))

# 4 - Desvio padrão
'''
Quanto mais próximo do 0 for o desvio padrão,
significa que os dados do conjunto estão menos dispersos
'''
print(statistics.stdev([1, 1, 1, 1.56, 2.37, 1,47]))