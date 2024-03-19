# Definicja funkcji rotate_list, która obraca listę o zadaną liczbę kroków w prawo
def rotate_list(lst, steps):
    if not lst:
        return []
    steps = steps % len(lst)  # Normalizacja liczby kroków, jeśli przekracza długość listy
    return lst[-steps:] + lst[:-steps]  # Obrót listy

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_list = [1, 2, 3, 4, 5]
# rotated_list = rotate_list(my_list, 2)
# print("Obrócona lista:", rotated_list)


my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 2)
print("Obrócona lista:", rotated_list)
