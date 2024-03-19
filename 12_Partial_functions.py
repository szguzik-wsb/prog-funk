from functools import partial

def multiply(x, y):
    return x * y

triple = partial(multiply, 3)

print(triple(10))  # Wypisze 30
