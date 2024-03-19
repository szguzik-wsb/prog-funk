# Definicja funkcji double_list_elements, która podwaja każdy element w przekazanej liście liczb
def double_list_elements(numbers):
    return [x * 2 for x in numbers]  # Tworzenie nowej listy poprzez podwojenie każdego elementu

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# original_list = [1, 2, 3, 4, 5]
# doubled_list = double_list_elements(original_list)
# print("Lista po podwojeniu:", doubled_list)





original_list = [1, 2, 3, 4, 5]
doubled_list = double_list_elements(original_list)

# Wynik działania funkcji
print("Oryginalna lista:", original_list)  # Oryginalna lista: [1, 2, 3, 4, 5]
print("Lista po podwojeniu:", doubled_list)  # Lista po podwojeniu: [2, 4, 6, 8, 10]
