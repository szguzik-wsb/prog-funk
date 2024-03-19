# Definicja funkcji remove_duplicates, która usuwa zduplikowane elementy z listy
# zachowując kolejność wystąpienia pierwszego wystąpienia każdego elementu.
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


original_list = [1, 2, 3, 2, 4, 5, 3, 6]
list_without_duplicates = remove_duplicates(original_list)

# Wynik działania funkcji
print("Oryginalna lista:", original_list)  # Oryginalna lista: [1, 2, 3, 2, 4, 5, 3, 6]
print("Lista bez duplikatów:", list_without_duplicates)  # Lista bez duplikatów: [1, 2, 3, 4, 5, 6]
