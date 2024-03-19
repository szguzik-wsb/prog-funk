def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Utworzenie generatora ciągu Fibonacciego
fibonacci_generator = generate_fibonacci()

# Przykładowe użycie generatora do wygenerowania pierwszych 10 liczb ciągu Fibonacciego
first_10_fibonacci_numbers = [next(fibonacci_generator) for _ in range(10)]

# Wynik działania generatora
print("Pierwsze 10 liczb ciągu Fibonacciego:", first_10_fibonacci_numbers)
