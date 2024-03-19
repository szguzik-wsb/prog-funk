is_palindrome = lambda s: s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")
print(is_palindrome("A man a plan a canal Panama"))  # True
