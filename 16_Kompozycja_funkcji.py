def add_five(x):
    return x + 5

def multiply_by_two(x):
    return x * 2

def compose(f, g):
    return lambda x: f(g(x))

add_then_multiply = compose(multiply_by_two, add_five)
print(add_then_multiply(10))  # Wypisze 30

# Objaśnienie: Kompozycja funkcji to proces tworzenia nowych funkcji przez łączenie dwóch lub więcej funkcji,
# gdzie wynik jednej funkcji staje się argumentem następnej.
# W tym przykładzie add_then_multiply dodaje najpierw 5 do liczby, a następnie mnoży wynik przez 2.