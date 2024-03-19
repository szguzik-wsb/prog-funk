from functools import partial

def add(x, y):
    return x + y

add_five = partial(add, 5)
print(add_five(10))  # Wypisze 15

# Objaśnienie: Aplikacja częściowa to proces tworzenia nowej funkcji przez predefiniowanie
# niektórych argumentów istniejącej funkcji.
# W tym przykładzie add_five jest nową funkcją,
# która dodaje 5 do swojego argumentu.