# Definicja funkcji zip_with_index, która łączy elementy listy z ich indeksami, tworząc krotki (indeks, element)
def zip_with_index(lst):
    return list(enumerate(lst))

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_list = ['a', 'b', 'c', 'd']
# indexed_list = zip_with_index(my_list)
# print("Lista z indeksami:", indexed_list)

my_list = ['a', 'b', 'c', 'd']
indexed_list = zip_with_index(my_list)
print("Lista z indeksami:", indexed_list)
