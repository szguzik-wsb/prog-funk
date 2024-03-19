from itertools import groupby
liczby = [1, 2, 3, 4, 5, 6, 7, 8]
zgrupowane_liczby = {k: list(v) for k, v in groupby(liczby, key=lambda x: x % 2)}
print(zgrupowane_liczby)  # {1: [1, 3, 5, 7], 0: [2, 4, 6, 8]}
