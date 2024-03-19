def generate_infinite_sequence():
    num = 0
    while True:
        yield num
        num += 2

generator = generate_infinite_sequence()

print(next(generator))  # Wypisze 0
print(next(generator))  # Wypisze 2


# Objaśnienie: Leniwe obliczanie (lazy evaluation) to strategia opóźniania obliczeń do momentu,
# gdy są one faktycznie potrzebne. Generatory w Pythonie umożliwiają leniwe generowanie wartości,
# co jest przydatne przy pracy z dużymi zbiorami danych lub nieskończonymi sekwencjami.