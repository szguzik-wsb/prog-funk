def calculate_factorial(n):
    if n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

print(calculate_factorial(5))

# Objaśnienie: Rekursja to technika programistyczna,
# gdzie funkcja wywołuje samą siebie. Jest często używana do rozwiązywania problemów,
# które można podzielić na podobne podproblemy mniejszej skali.
# W tym przypadku funkcja calculate_factorial oblicza silnię liczby n.
