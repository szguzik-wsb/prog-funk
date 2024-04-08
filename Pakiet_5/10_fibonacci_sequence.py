def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.rstrip()


# Przykładowe użycie dla generatora sekwencji Fibonacciego
fib = fibonacci_sequence()
for _ in range(10):
    print(next(fib))

# Przykładowe użycie dla czytania dużego pliku
# for line in read_large_file("large_file.txt"):
#    process(line)  # podstawowym założeniem jest tutaj, że funkcja process() istnieje i obsługuje linię tekstu
