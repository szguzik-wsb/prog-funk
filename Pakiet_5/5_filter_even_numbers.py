def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


rect_area = lambda length, width: length * width

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # wypisze: [2, 4, 6]
print(rect_area(10, 5))  # wypisze: 50
