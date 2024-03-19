# Definicja funkcji find_max_min_diff, która znajduje różnicę między maksymalną a minimalną wartością w liście
def find_max_min_diff(lst):
    if not lst:  # Sprawdzenie, czy lista nie jest pusta
        return None
    return max(lst) - min(lst)  # Obliczenie różnicy między maksymalną a minimalną wartością

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# numbers = [10, 4, 5, 24, 6, 1, 3]
# diff = find_max_min_diff(numbers)
# print("Różnica między maksymalną a minimalną wartością:", diff)



numbers = [10, 4, 5, 24, 6, 1, 3]
diff = find_max_min_diff(numbers)
print("Różnica między maksymalną a minimalną wartością:", diff)
