def make_multiplier(x):
    def multipliter(n):
        return x * n

    return multipliter


double = make_multiplier(2)

print(double(5))
