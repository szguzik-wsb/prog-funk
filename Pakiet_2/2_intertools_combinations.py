from itertools import combinations
def wszystkie_kombinacje(elementy):
    return list(combinations(elementy, 2))

przykladowa_lista = [1, 2, 3, 4]
print(wszystkie_kombinacje(przykladowa_lista))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
