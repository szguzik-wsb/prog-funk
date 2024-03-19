# Definicja funkcji filter_long_words, która filtruje stringi dłuższe niż średnia długość wszystkich stringów w liście
def filter_long_words(strings):
    average_length = sum(len(s) for s in strings) / len(strings)  # Obliczenie średniej długości stringów
    return [s for s in strings if len(s) > average_length]  # Filtracja stringów dłuższych niż średnia długość

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# string_list = ["hello", "world", "Python", "is", "awesome"]
# filtered_list = filter_long_words(string_list)
# print("Filtrowana lista:", filtered_list)



string_list = ["hello", "world", "Python", "is", "awesome"]
filtered_list = filter_long_words(string_list)

# Wynik działania funkcji
print("Oryginalna lista:", string_list)  # Oryginalna lista: ["hello", "world", "Python", "is", "awesome"]
print("Filtrowana lista:", filtered_list)  # Filtrowana lista: ["Python", "awesome"]
