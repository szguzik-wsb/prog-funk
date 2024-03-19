def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
pierwsze_10_fib = [next(fib) for _ in range(10)]
print(pierwsze_10_fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
