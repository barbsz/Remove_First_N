def remove_chars(string, n):
    n = min(n, len(string))
    return string[n:]

input_string = "Hello, World"
n = 5

result = remove_chars(input_string, n)
print("New string:", result)
