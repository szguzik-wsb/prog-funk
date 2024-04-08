from itertools import groupby

liczby = [1, 2, 3, 4, 5, 6, 7, 8]

# Sortujemy liczby według parzystości, aby `groupby` działało prawidłowo
liczby_posortowane = sorted(liczby, key=lambda x: x % 2)

# Grupujemy posortowane liczby na podstawie ich parzystości
zgrupowane_liczby = {k: list(v) for k, v in groupby(liczby_posortowane, key=lambda x: x % 2)}

print(zgrupowane_liczby)
