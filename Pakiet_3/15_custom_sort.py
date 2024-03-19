# Definicja funkcji custom_sort, która sortuje listę według zadanej funkcji klucza
def custom_sort(lst, key_func):
    # Używanie funkcji wbudowanej sorted z kluczem sortowania
    return sorted(lst, key=key_func)

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_list = ['banana', 'apple', 'cherry', 'date']
# sorted_list = custom_sort(my_list, key_func=len)
# print("Posortowana lista:", sorted_list)

my_list = ['banana', 'apple', 'cherry', 'date']
sorted_list = custom_sort(my_list, key_func=len)
print("Posortowana lista:", sorted_list)
