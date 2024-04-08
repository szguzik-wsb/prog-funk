def sum_even_numbers(num_list):
    return sum(num for num in num_list if num % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers)
print(result)
