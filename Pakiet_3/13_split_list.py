# Definicja funkcji split_list, która dzieli listę na podlisty o zadanej długości
def split_list(lst, length):
    # Używanie list comprehension do stworzenia podlist o zadanej długości
    return [lst[i:i+length] for i in range(0, len(lst), length)]

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# split_lists = split_list(my_list, 3)
# print("Podzielona lista:", split_lists)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
split_lists = split_list(my_list, 3)
print("Podzielona lista:", split_lists)
