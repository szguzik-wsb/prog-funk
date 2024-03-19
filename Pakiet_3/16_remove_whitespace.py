# Definicja funkcji remove_whitespace, która usuwa białe znaki z każdego elementu listy stringów
def remove_whitespace(string_list):
    # Używanie metody strip do usunięcia białych znaków z każdego elementu listy
    return [s.strip() for s in string_list]

# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# my_strings = ['  hello ', 'world!  ', '  python  ']
# no_whitespace_list = remove_whitespace(my_strings)
# print("Lista bez białych znaków:", no_whitespace_list)

my_strings = ['  hello ', 'world!  ', '  python  ']
no_whitespace_list = remove_whitespace(my_strings)
print("Lista bez białych znaków:", no_whitespace_list)
