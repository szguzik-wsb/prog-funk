# Definicja funkcji recursive_sum, która oblicza sumę wszystkich liczb w zagnieżdżonej liście
def recursive_sum(numbers):
    total_sum = 0
    for element in numbers:
        # Sprawdzenie, czy element jest listą - jeśli tak, wywołanie funkcji rekurencyjnie
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element
    return total_sum

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# nested_list = [1, 2, [3, 4], [5, [6, 7]], 8]
# total_sum = recursive_sum(nested_list)
# print("Suma wszystkich liczb:", total_sum)



nested_list = [1, 2, [3, 4], [5, [6, 7]], 8]
total_sum = recursive_sum(nested_list)

# Wynik działania funkcji
print("Zagnieżdżona lista:", nested_list)  # Zagnieżdżona lista: [1, 2, [3, 4], [5, [6, 7]], 8]
print("Suma wszystkich liczb:", total_sum)  # Suma wszystkich liczb: 36
