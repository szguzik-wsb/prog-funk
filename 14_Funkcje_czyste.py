def multiply(x, y):
    return x * y

result = multiply(2, 3)
print(result)

# Objaśnienie: Funkcje czyste to takie,
# które dla tych samych argumentów zawsze zwracają
# tę samą wartość i nie mają żadnych efektów ubocznych
# (np. nie modyfikują zmiennych globalnych).
# Funkcja multiply jest przykładem funkcji czystej.