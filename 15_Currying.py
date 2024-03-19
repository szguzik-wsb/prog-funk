def add(x):
    def inner(y):
        return x + y
    return inner

add_five = add(5)
print(add_five(10))  # Wypisze 15

# Objaśnienie: Currying to technika przekształcania funkcji z wieloma argumentami w ciąg funkcji,
# z których każda przyjmuje jeden argument.
# W tym przykładzie funkcja add przekształca się w funkcję, która dodaje 5 do swojego argumentu.