# Definicja funkcji count_unique_elements, która zlicza unikalne elementy w liście
def count_unique_elements(lst):
    # Używanie zbioru do znalezienia unikalnych elementów, a następnie zliczanie ich liczby
    unique_elements = set(lst)
    return len(unique_elements)

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# unique_count = count_unique_elements(my_list)
# print("Liczba unikalnych elementów:", unique_count)


my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_count = count_unique_elements(my_list)
print("Liczba unikalnych elementów:", unique_count)
