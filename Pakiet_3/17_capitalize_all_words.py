# Definicja funkcji capitalize_all_words, która zamienia pierwszą literę każdego słowa w stringu na wielką literę
def capitalize_all_words(s):
    # Używanie metody title do zamiany pierwszej litery każdego słowa na wielką literę
    return s.title()

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_string = "hello world! python is great."
# capitalized_string = capitalize_all_words(my_string)
# print("String po kapitalizacji:", capitalized_string)


my_string = "hello world! python is great."
capitalized_string = capitalize_all_words(my_string)
print("String po kapitalizacji:", capitalized_string)
