def outer_function(text):
    # Zmienna globalna
    global outer_var
    outer_var = "Jestem zmienną zewnętrzną"

    def inner_function(inner_text):
        # Zamknięcie (closure) - funkcja wewnętrzna korzysta ze zmiennej z funkcji zewnętrznej
        return text + " " + inner_text

    return inner_function


func = outer_function("Witaj,")
print(func("świecie!"))  # wypisze: "- Witaj, świecie"
