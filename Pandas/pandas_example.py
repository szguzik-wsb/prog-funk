import pandas as pd
import numpy as np

# Tworzenie serii pandas
ser = pd.Series([1, 2, 3, 4, 5])
print("1. Tworzenie serii pandas:")
print(ser)

# Tworzenie serii pandas z datami
dates = pd.date_range('20230101', periods=5)
ser = pd.Series([1, 2, 3, 4, 5], index=dates)
print("\n2. Tworzenie serii pandas z datami:")
print(ser)

# Tworzenie ramki danych pandas
df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
print("\n3. Tworzenie ramki danych pandas:")
print(df)

# Tworzenie ramki danych pandas z słownika
data = {'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']}
df = pd.DataFrame(data)
print("\n4. Tworzenie ramki danych pandas z słownika:")
print(df)

# Transpozycja ramki danych
df_transposed = df.T
print("\n5. Transpozycja ramki danych:")
print(df_transposed)

# Wybieranie kolumny z ramki danych
col = df['A']
print("\n6. Wybieranie kolumny z ramki danych:")
print(col)

# Wybieranie wiersza z ramki danych
row = df.loc[0]
print("\n7. Wybieranie wiersza z ramki danych:")
print(row)

# Wybieranie fragmentu ramki danych
subset = df.loc[0:2, ['A', 'B']]
print("\n8. Wybieranie fragmentu ramki danych:")
print(subset)

# Zmiana nazw kolumn w ramce danych
df.columns = ['X', 'Y']
print("\n9. Zmiana nazw kolumn w ramce danych:")
print(df)

# Zmiana indeksu w ramce danych
df.index = pd.date_range('20230101', periods=4)
print("\n10. Zmiana indeksu w ramce danych:")
print(df)

# Sortowanie ramki danych względem wartości w kolumnie
df_sorted = df.sort_values(by='X')
print("\n11. Sortowanie ramki danych względem wartości w kolumnie:")
print(df_sorted)

# Dodawanie nowej kolumny do ramki danych
df['Z'] = np.random.rand(4)
print("\n12. Dodawanie nowej kolumny do ramki danych:")
print(df)

# Usuwanie kolumny z ramki danych
df = df.drop(columns=['Z'])
print("\n13. Usuwanie kolumny z ramki danych:")
print(df)

# Łączenie ramek danych wzdłuż kolumn
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
concatenated_df = pd.concat([df1, df2])
print("\n14. Łączenie ramek danych wzdłuż kolumn:")
print(concatenated_df)

# Łączenie ramek danych wzdłuż wierszy
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
concatenated_df = pd.concat([df1, df2], axis=1)
print("\n15. Łączenie ramek danych wzdłuż wierszy:")
print(concatenated_df)

# Łączenie ramek danych za pomocą kluczy
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
merged_df = pd.merge(df1, df2, on='A')
print("\n16. Łączenie ramek danych za pomocą kluczy:")
print(merged_df)

# Grupowanie danych w ramce danych
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)
grouped = df.groupby('A').sum()
print("\n17. Grupowanie danych w ramce danych:")
print(grouped)

# Wykonanie funkcji na grupach w ramce danych
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)
grouped = df.groupby('A').apply(lambda x: x['C'].sum())
print("\n18. Wykonanie funkcji na grupach w ramce danych:")
print(grouped)

# Łączenie ramek danych metodą join
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=['a', 'b', 'd'])
joined_df = df1.join(df2, how='outer')
print("\n19. Łączenie ramek danych metodą join:")
print(joined_df)

# Usuwanie wierszy z brakującymi danymi
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4]})
cleaned_df = df.dropna()
print("\n20. Usuwanie wierszy z brakującymi danymi:")
print(cleaned_df)

# Uzupełnianie brakujących danych wartościami
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4]})
filled_df = df.fillna(0)
print("\n21. Uzupełnianie brakujących danych wartościami:")
print(filled_df)

# Usuwanie duplikatów w ramce danych
df = pd.DataFrame({'A': [1, 2, 2, 3, 4], 'B': ['a', 'b', 'b', 'c', 'd']})
unique_df = df.drop_duplicates()
print("\n22. Usuwanie duplikatów w ramce danych:")
print(unique_df)

# Resetowanie indeksu w ramce danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
reset_index_df = df.reset_index()
print("\n23. Resetowanie indeksu w ramce danych:")
print(reset_index_df)

# Zamiana kolumny w ramce danych na indeks
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.set_index('A', inplace=True)
print("\n24. Zamiana kolumny w ramce danych na indeks:")
print(df)

# Zamiana typu danych kolumny w ramce danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['4', '5', '6']})
df['B'] = df['B'].astype(int)
print("\n25. Zamiana typu danych kolumny w ramce danych:")
print(df)

# Obliczanie statystyk opisowych dla ramki danych
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
statistics = df.describe()
print("\n26. Obliczanie statystyk opisowych dla ramki danych:")
print(statistics)

# Obliczanie korelacji między kolumnami ramki danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
correlation = df.corr()
print("\n27. Obliczanie korelacji między kolumnami ramki danych:")
print(correlation)

# Obliczanie kowariancji między kolumnami ramki danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
covariance = df.cov()
print("\n28. Obliczanie kowariancji między kolumnami ramki danych:")
print(covariance)

# Obliczanie iloczynu skalarnego między kolumnami ramki danych
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
dot_product = df1.dot(df2.T)
print("\n29. Obliczanie iloczynu skalarnego między kolumnami ramki danych:")
print(dot_product)

# Zmiana wartości w ramce danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.loc[0, 'A'] = 10
print("\n30. Zmiana wartości w ramce danych:")
print(df)

# Wycinanie ramki danych
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
sliced_df = df[1:3]
print("\n31. Wycinanie ramki danych:")
print(sliced_df)

# Filtrowanie ramki danych
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
filtered_df = df[df['A'] > 2]
print("\n32. Filtrowanie ramki danych:")
print(filtered_df)

# Zmiana kolejności kolumn w ramce danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
reordered_columns_df = df[['B', 'A']]
print("\n33. Zmiana kolejności kolumn w ramce danych:")
print(reordered_columns_df)

# Zmiana kolejności wierszy w ramce danych
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['c', 'b', 'a'])
sorted_index_df = df.sort_index()
print("\n34. Zmiana kolejności wierszy w ramce danych:")
print(sorted_index_df)

# Usuwanie kolumn o brakujących danych
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
dropped_na_df = df.dropna(axis=1)
print("\n35. Usuwanie kolumn o brakujących danych:")
print(dropped_na_df)

# Usuwanie wierszy o brakujących danych
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
dropped_na_df = df.dropna(axis=0)
print("\n36. Usuwanie wierszy o brakujących danych:")
print(dropped_na_df)

# Uzupełnianie brakujących danych w ramce danych
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
filled_na_df = df.fillna(0)
print("\n37. Uzupełnianie brakujących danych w ramce danych:")
print(filled_na_df)

# Uzupełnianie brakujących danych w ramce danych metodą interpolacji
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4]})
interpolated_df = df.interpolate()
print("\n38. Uzupełnianie brakujących danych w ramce danych metodą interpolacji:")
print(interpolated_df)

# Dodawanie nowej kolumny do ramki danych za pomocą funkcji
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print("\n39. Dodawanie nowej kolumny do ramki danych za pomocą funkcji:")
print(df)

# Wybieranie wierszy na podstawie warunku
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})
filtered_df = df[df['A'] > 2]
print("\n40. Wybieranie wierszy na podstawie warunku:")
print(filtered_df)

# Zmiana typu danych kolumny w ramce danych na kategoryczny
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})
df['B'] = df['B'].astype('category')
print("\n41. Zmiana typu danych kolumny w ramce danych na kategoryczny:")
print(df)

# Łączenie ramek danych metodą concat
df1 = pd.DataFrame({'A': [1, 2], 'B': ['a', 'b']})
df2 = pd.DataFrame({'A': [3, 4], 'B': ['c', 'd']})
appended_df = pd.concat([df1, df2])
print("\n42. Łączenie ramek danych metodą concat:")
print(appended_df)

# Łączenie ramek danych metodą merge
df1 = pd.DataFrame({'A': [1, 2], 'B': ['a', 'b']})
df2 = pd.DataFrame({'A': [1, 2], 'C': ['c', 'd']})
merged_df = pd.merge(df1, df2, on='A')
print("\n43. Łączenie ramek danych metodą merge:")
print(merged_df)

# Tworzenie tabeli przestawnej na podstawie ramki danych
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(values='C', index='A', columns='B', aggfunc=np.sum)
print("\n44. Tworzenie tabeli przestawnej na podstawie ramki danych:")
print(pivot_table)

# Zapisywanie ramki danych do pliku CSV
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.to_csv('data.csv', index=False)
print("\n45. Zapisywanie ramki danych do pliku CSV: (plik 'data.csv' został zapisany)")

# Odczytywanie danych z pliku CSV do ramki danych
df = pd.read_csv('data.csv')
print("\n46. Odczytywanie danych z pliku CSV do ramki danych:")
print(df)
