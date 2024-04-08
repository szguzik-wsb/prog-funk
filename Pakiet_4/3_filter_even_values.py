def filter_even_values(d):
    return {k: v for k, v in d.items() if v % 2 == 0}


# Użycie:
print(filter_even_values({"a": 1, "b": 2, "c": 3, "d": 4}))  # wypisze: {"b": 2, "d": 4}
