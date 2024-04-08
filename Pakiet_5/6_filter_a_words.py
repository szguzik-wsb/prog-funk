def filter_a_words(words):
    return list(filter(lambda x: x.startswith('a'), words))


def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))


print(filter_a_words(["apple", "banana", "avocado", "cherry"]))  # wypisze: ["apple", "avocado"]
print(square_numbers([1, 2, 3, 4]))  # wypisze: [1, 4, 9, 16]
