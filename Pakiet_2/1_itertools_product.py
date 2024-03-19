from itertools import product
list_1 = ['A', 'B']
list_2 = ['C', 'D']
kombinacje = list(product(list_1, list_2))
print(kombinacje)  # [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]