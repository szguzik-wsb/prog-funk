def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Błąd: {e}")
            return None
    return wrapper

@safe_function
def dziel(a, b):
    return a / b

print(dziel(10, 2))  # 5.0
print(dziel(10, 0))  # Błąd: division by zero, None
