# Definicja funkcji transpose_matrix, która transponuje macierz (zamienia wiersze na kolumny i odwrotnie)
def transpose_matrix(matrix):
    # Używanie list comprehension do transponowania macierzy
    return [list(row) for row in zip(*matrix)]

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transposed_matrix = transpose_matrix(my_matrix)
# print("Transponowana macierz:", transposed_matrix)

my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose_matrix(my_matrix)
print("Transponowana macierz:", transposed_matrix)
