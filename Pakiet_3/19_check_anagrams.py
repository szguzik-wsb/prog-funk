# Definicja funkcji check_anagrams, która sprawdza, czy dwa podane stringi są anagramami
def check_anagrams(str1, str2):
    # Usunięcie białych znaków i zamiana na małe litery
    clean_str1 = ''.join(str1.split()).lower()
    clean_str2 = ''.join(str2.split()).lower()

    # Sprawdzenie, czy posortowane stringi są takie same
    return sorted(clean_str1) == sorted(clean_str2)


# Teraz funkcja została zdefiniowana, ale nie wywołana. Można ją wywołać w razie potrzeby, na przykład:
# str1 = "Listen"
# str2 = "Silent"
# are_anagrams = check_anagrams(str1, str2)
# print(f"'{str1}' i '{str2}' są anagramami:", are_anagrams)


str1 = "Listen"
str2 = "Silent"
are_anagrams = check_anagrams(str1, str2)
print(f"'{str1}' i '{str2}' są anagramami:", are_anagrams)
