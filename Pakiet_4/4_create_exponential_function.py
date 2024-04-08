def create_exponential_function(exponent):
    return lambda x: x ** exponent


# Użycie:
square = create_exponential_function(2)
print(square(3))  # wypisze: 9
