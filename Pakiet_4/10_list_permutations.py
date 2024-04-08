from itertools import permutations


def list_permutations(lst):
    return list(permutations(lst))


# Użycie:
print(list_permutations([1, 2, 3]))  # wypisze: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
