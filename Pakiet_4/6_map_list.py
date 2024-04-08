def map_list(lst, func):
    return [func(x) for x in lst]


# Użycie:
print(map_list([1, 2, 3, 4], lambda x: x * 2))  # wypisze: [2, 4, 6, 8]
