# Definicja funkcji sum_of_squares_of_odds, która oblicza sumę kwadratów liczb nieparzystych z listy
def sum_of_squares_of_odds(numbers):
    # Używanie list comprehension do znalezienia kwadratów liczb nieparzystych, a następnie sumowanie ich
    return sum(x**2 for x in numbers if x % 2 != 0)

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_numbers = [1, 2, 3, 4, 5]
# sum_squares = sum_of_squares_of_odds(my_numbers)
# print("Suma kwadratów liczb nieparzystych:", sum_squares)


my_numbers = [1, 2, 3, 4, 5]
sum_squares = sum_of_squares_of_odds(my_numbers)
print("Suma kwadratów liczb nieparzystych:", sum_squares)
