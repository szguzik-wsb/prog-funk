import numpy as np

# Tworzenie tablicy numpy
arr = np.array([1, 2, 3, 4, 5])
print("1. Tworzenie tablicy numpy:")
print(arr)

# Tworzenie tablicy z sekwencją liczb
arr = np.arange(0, 10, 2)
print("\n2. Tworzenie tablicy z sekwencją liczb:")
print(arr)

# Tworzenie tablicy z równomiernie rozmieszczonymi wartościami
arr = np.linspace(0, 10, 5)
print("\n3. Tworzenie tablicy z równomiernie rozmieszczonymi wartościami:")
print(arr)

# Tworzenie tablicy wypełnionej zerami
arr = np.zeros((2, 3))
print("\n4. Tworzenie tablicy wypełnionej zerami:")
print(arr)

# Tworzenie tablicy wypełnionej jedynkami
arr = np.ones((3, 2))
print("\n5. Tworzenie tablicy wypełnionej jedynkami:")
print(arr)

# Tworzenie macierzy jednostkowej
arr = np.eye(3)
print("\n6. Tworzenie macierzy jednostkowej:")
print(arr)

# Tworzenie tablicy z losowymi wartościami z rozkładu jednostajnego
arr = np.random.rand(2, 2)
print("\n7. Tworzenie tablicy z losowymi wartościami z rozkładu jednostajnego:")
print(arr)

# Tworzenie tablicy z losowymi wartościami z rozkładu normalnego
arr = np.random.randn(2, 2)
print("\n8. Tworzenie tablicy z losowymi wartościami z rozkładu normalnego:")
print(arr)

# Tworzenie tablicy z losowymi liczbami całkowitymi
arr = np.random.randint(1, 10, (3, 3))
print("\n9. Tworzenie tablicy z losowymi liczbami całkowitymi:")
print(arr)

# Zmiana kształtu tablicy
arr = np.arange(1, 10).reshape(3, 3)
print("\n10. Zmiana kształtu tablicy:")
print(arr)

# Transpozycja tablicy
arr = np.array([[1, 2], [3, 4]])
arr_transpose = np.transpose(arr)
print("\n11. Transpozycja tablicy:")
print(arr_transpose)

# Sumowanie elementów tablicy
arr = np.array([[1, 2], [3, 4]])
total_sum = np.sum(arr)
print("\n12. Sumowanie elementów tablicy:")
print(total_sum)

# Obliczanie średniej wartości
arr = np.array([[1, 2], [3, 4]])
mean_value = np.mean(arr)
print("\n13. Obliczanie średniej wartości:")
print(mean_value)

# Obliczanie mediany wartości
arr = np.array([[1, 2], [3, 4]])
median_value = np.median(arr)
print("\n14. Obliczanie mediany wartości:")
print(median_value)

# Obliczanie odchylenia standardowego
arr = np.array([[1, 2], [3, 4]])
std_deviation = np.std(arr)
print("\n15. Obliczanie odchylenia standardowego:")
print(std_deviation)

# Obliczanie wariancji
arr = np.array([[1, 2], [3, 4]])
variance = np.var(arr)
print("\n16. Obliczanie wariancji:")
print(variance)

# Znajdowanie najmniejszej wartości
arr = np.array([[1, 2], [3, 4]])
min_value = np.min(arr)
print("\n17. Znajdowanie najmniejszej wartości:")
print(min_value)

# Znajdowanie największej wartości
arr = np.array([[1, 2], [3, 4]])
max_value = np.max(arr)
print("\n18. Znajdowanie największej wartości:")
print(max_value)

# Znajdowanie indeksu najmniejszej wartości
arr = np.array([4, 2, 7, 1])
min_index = np.argmin(arr)
print("\n19. Znajdowanie indeksu najmniejszej wartości:")
print(min_index)

# Znajdowanie indeksu największej wartości
arr = np.array([4, 2, 7, 1])
max_index = np.argmax(arr)
print("\n20. Znajdowanie indeksu największej wartości:")
print(max_index)

# Ograniczanie wartości do określonego zakresu
arr = np.array([1, 2, 3, 4, 5])
arr_clipped = np.clip(arr, 2, 4)
print("\n21. Ograniczanie wartości do określonego zakresu:")
print(arr_clipped)

# Znajdowanie unikalnych wartości
arr = np.array([1, 2, 2, 3, 3, 4, 5])
unique_values = np.unique(arr)
print("\n22. Znajdowanie unikalnych wartości:")
print(unique_values)

# Łączenie tablic
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2))
print("\n23. Łączenie tablic:")
print(concatenated_arr)

# Łączenie tablic w pionie (po wierszach)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
stacked_arr = np.vstack((arr1, arr2))
print("\n24. Łączenie tablic w pionie:")
print(stacked_arr)

# Łączenie tablic w poziomie (po kolumnach)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5], [6]])
stacked_arr = np.hstack((arr1, arr2))
print("\n25. Łączenie tablic w poziomie:")
print(stacked_arr)

# Dzielenie tablicy na podtablice
arr = np.array([1, 2, 3, 4, 5, 6])
subarrays = np.split(arr, 3)
print("\n26. Dzielenie tablicy na podtablice:")
print(subarrays)

# Znajdowanie indeksów, gdzie spełniony jest warunek
arr = np.array([1, 2, 3, 4, 5])
indices = np.where(arr > 2)
print("\n27. Znajdowanie indeksów, gdzie spełniony jest warunek:")
print(indices)

# Obliczanie średniej ważonej
arr = np.array([1, 2, 3, 4])
weights = np.array([1, 2, 3, 4])
weighted_mean = np.average(arr, weights=weights)
print("\n28. Obliczanie średniej ważonej:")
print(weighted_mean)

# Mnożenie macierzy
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr1, arr2)
print("\n29. Mnożenie macierzy:")
print(dot_product)

# Obliczanie iloczynu wektorowego
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
cross_product = np.cross(arr1, arr2)
print("\n30. Obliczanie iloczynu wektorowego:")
print(cross_product)

# Obliczanie macierzy odwrotnej
arr = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(arr)
print("\n31. Obliczanie macierzy odwrotnej:")
print(inverse_matrix)

# Obliczanie wyznacznika macierzy
arr = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(arr)
print("\n32. Obliczanie wyznacznika macierzy:")
print(determinant)

# Obliczanie wartości własnych i wektorów własnych macierzy
arr = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(arr)
print("\n33. Obliczanie wartości własnych i wektorów własnych macierzy:")
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Znajdowanie rozkładu wartości osobliwych
arr = np.array([[1, 2], [3, 4]])
U, S, V = np.linalg.svd(arr)
print("\n34. Znajdowanie rozkładu wartości osobliwych:")
print("U:", U)
print("S:", S)
print("V:", V)

# Transformata Fouriera
arr = np.array([1, 2, 3, 4])
fft_result = np.fft.fft(arr)
print("\n35. Transformata Fouriera:")
print(fft_result)

# Odwrotna transformata Fouriera
arr = np.array([1, 2, 3, 4])
ifft_result = np.fft.ifft(arr)
print("\n36. Odwrotna transformata Fouriera:")
print(ifft_result)

# Splot dwóch sygnałów
arr1 = np.array([1, 2, 3])
arr2 = np.array([0, 1, 0.5])
convolution_result = np.convolve(arr1, arr2, mode='full')
print("\n37. Splot dwóch sygnałów:")
print(convolution_result)

# Obliczanie korelacji dwóch sygnałów
arr1 = np.array([1, 2, 3])
arr2 = np.array([0, 1, 0.5])
correlation_result = np.correlate(arr1, arr2, mode='full')
print("\n38. Obliczanie korelacji dwóch sygnałów:")
print(correlation_result)

# Obliczanie macierzy kowariancji
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 3, 4])
covariance_matrix = np.cov(arr1, arr2)
print("\n39. Obliczanie macierzy kowariancji:")
print(covariance_matrix)

# Tworzenie histogramu
arr = np.array([1, 1, 2, 3, 4, 5])
hist, bins = np.histogram(arr, bins=3)
print("\n40. Tworzenie histogramu:")
print("Histogram:", hist)
print("Bins:", bins)

# Liczenie wystąpień poszczególnych wartości
arr = np.array([1, 1, 2, 3, 3, 3])
counts = np.bincount(arr)
print("\n41. Liczenie wystąpień poszczególnych wartości:")
print(counts)

# Znajdowanie unikalnych wartości i ich liczebności
arr = np.array([1, 1, 2, 3, 3, 3])
unique_values, counts = np.unique(arr, return_counts=True)
print("\n42. Znajdowanie unikalnych wartości i ich liczebności:")
print("Unique values:", unique_values)
print("Counts:", counts)

# Znajdowanie indeksu, gdzie należy wstawić wartość, aby zachować porządek
arr = np.array([1, 3, 5, 7])
index = np.searchsorted(arr, 6)
print("\n43. Znajdowanie indeksu, gdzie należy wstawić wartość, aby zachować porządek:")
print(index)

# Obliczanie różnic między kolejnymi elementami
arr = np.array([1, 3, 6, 10])
differences = np.diff(arr)
print("\n44. Obliczanie różnic między kolejnymi elementami:")
print(differences)

# Obliczanie gradientu
arr = np.array([1, 2, 4, 7])
gradient = np.gradient(arr)
print("\n45. Obliczanie gradientu:")
print(gradient)

# Dopasowywanie wielomianu do danych
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 0.8, 0.9, 0.1, -0.8])
coefficients = np.polyfit(x, y, 2)
print("\n46. Dopasowywanie wielomianu do danych:")
print(coefficients)

# Obliczanie wartości wielomianu w danym punkcie
coefficients = [1, 2, 1]
value = np.polyval(coefficients, 2)
print("\n47. Obliczanie wartości wielomianu w danym punkcie:")
print(value)

# Znajdowanie pierwiastków wielomianu
coefficients = [1, -3, 2]
roots = np.roots(coefficients)
print("\n48. Znajdowanie pierwiastków wielomianu:")
print(roots)

# Obliczanie całki numerycznej z danych
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
integral = np.trapz(y, x)
print("\n49. Obliczanie całki numerycznej z danych:")
print(integral)

# Obliczanie skumulowanej sumy
arr = np.array([1, 2, 3, 4])
cumulative_sum = np.cumsum(arr)
print("\n50. Obliczanie skumulowanej sumy:")
print(cumulative_sum)

# Obliczanie skumulowanego iloczynu
arr = np.array([1, 2, 3, 4])
cumulative_product = np.cumprod(arr)
print("\n51. Obliczanie skumulowanego iloczynu:")
print(cumulative_product)

# Obliczanie iloczynu wszystkich elementów
arr = np.array([1, 2, 3, 4])
product = np.prod(arr)
print("\n52. Obliczanie iloczynu wszystkich elementów:")
print(product)

# Obliczanie iloczynu wszystkich elementów, ignorując wartości NaN
arr = np.array([1, 2, np.nan, 4])
product = np.nanprod(arr)
print("\n53. Obliczanie iloczynu wszystkich elementów, ignorując wartości NaN:")
print(product)

# Sprawdzanie, czy wszystkie elementy spełniają warunek
arr = np.array([True, False, True])
result = np.all(arr)
print("\n54. Sprawdzanie, czy wszystkie elementy spełniają warunek:")
print(result)

# Sprawdzanie, czy jakikolwiek element spełnia warunek
arr = np.array([True, False, True])
result = np.any(arr)
print("\n55. Sprawdzanie, czy jakikolwiek element spełnia warunek:")
print(result)

# Zwracanie wartości z dwóch tablic w zależności od warunku
arr = np.array([1, 2, 3, 4])
result = np.where(arr > 2, arr, 0)
print("\n56. Zwracanie wartości z dwóch tablic w zależności od warunku:")
print(result)

# Sprawdzanie, czy wartość jest NaN
arr = np.array([1, np.nan, 3])
result = np.isnan(arr)
print("\n57. Sprawdzanie, czy wartość jest NaN:")
print(result)

# Sprawdzanie, czy wartość jest nieskończonością
arr = np.array([1, np.inf, 3])
result = np.isinf(arr)
print("\n58. Sprawdzanie, czy wartość jest nieskończonością:")
print(result)

# Sprawdzanie, czy wartość jest skończona
arr = np.array([1, np.inf, 3])
result = np.isfinite(arr)
print("\n59. Sprawdzanie, czy wartość jest skończona:")
print(result)

# Sortowanie tablicy
arr = np.array([3, 1, 2])
sorted_arr = np.sort(arr)
print("\n60. Sortowanie tablicy:")
print(sorted_arr)

# Zwracanie indeksów, które posortują tablicę
arr = np.array([3, 1, 2])
indices = np.argsort(arr)
print("\n61. Zwracanie indeksów, które posortują tablicę:")
print(indices)

# Wykonywanie cząstkowego sortowania tablicy
arr = np.array([3, 1, 2])
partitioned_arr = np.partition(arr, 2)
print("\n62. Wykonywanie cząstkowego sortowania tablicy:")
print(partitioned_arr)

# Zwracanie indeksów, które wykonają cząstkowe sortowanie tablicy
arr = np.array([3, 1, 2])
indices = np.argpartition(arr, 2)
print("\n63. Zwracanie indeksów, które wykonają cząstkowe sortowanie tablicy:")
print(indices)

# Znajdowanie unikalnych wartości zliczone w tablicy
arr = np.array([1, 1, 2, 3, 3, 3])
unique_values, counts = np.unique(arr, return_counts=True)
print("\n64. Znajdowanie unikalnych wartości zliczone w tablicy:")
print("Unique values:", unique_values)
print("Counts:", counts)

# Kopiowanie tablicy
arr = np.array([1, 2, 3])
tiled_arr = np.tile(arr, 2)
print("\n65. Kopiowanie tablicy:")
print(tiled_arr)

# Powtarzanie elementów tablicy
arr = np.array([1, 2, 3])
repeated_arr = np.repeat(arr, 3)
print("\n66. Powtarzanie elementów tablicy:")
print(repeated_arr)

# Wybieranie elementów z tablicy według indeksów
arr = np.array([1, 2, 3, 4])
indices = [0, 2]
selected_elements = np.take(arr, indices)
print("\n67. Wybieranie elementów z tablicy według indeksów:")
print(selected_elements)

# Wybieranie elementów z kilku tablic
choices = [0, 1, 2, 3]
index = [2, 3]
result = np.choose(index, choices)
print("\n68. Wybieranie elementów z kilku tablic:")
print(result)

# Ograniczanie wartości tablicy
arr = np.array([1, 2, 3, 4, 5])
clipped_arr = np.clip(arr, 2, 4)
print("\n69. Ograniczanie wartości tablicy:")
print(clipped_arr)

# Usuwanie elementów z tablicy
arr = np.array([1, 2, 3, 4, 5])
new_arr = np.delete(arr, [0, 4])
print("\n70. Usuwanie elementów z tablicy:")
print(new_arr)

# Wstawianie elementów do tablicy
arr = np.array([1, 2, 4, 5])
new_arr = np.insert(arr, 2, 3)
print("\n71. Wstawianie elementów do tablicy:")
print(new_arr)

# Dołączanie elementów do tablicy
arr = np.array([1, 2, 3])
new_arr = np.append(arr, [4, 5])
print("\n72. Dołączanie elementów do tablicy:")
print(new_arr)

# Zmiana rozmiaru tablicy
arr = np.array([1, 2, 3])
resized_arr = np.resize(arr, (5,))
print("\n73. Zmiana rozmiaru tablicy:")
print(resized_arr)

# Spłaszczanie tablicy wielowymiarowej do jednowymiarowej
arr = np.array([[1, 2], [3, 4]])
flattened_arr = arr.flatten()
print("\n74. Spłaszczanie tablicy wielowymiarowej do jednowymiarowej:")
print(flattened_arr)

# Transpozycja tablicy
arr = np.array([[1, 2], [3, 4]])
transposed_arr = arr.T
print("\n75. Transpozycja tablicy:")
print(transposed_arr)
