def even_numbers_generator():
    n = 0
    while True:
        yield n
        n += 2

# Przykładowe użycie generatora do wygenerowania pierwszych 5 liczb parzystych
gen = even_numbers_generator()
first_5_evens = [next(gen) for _ in range(5)]
first_5_evens
