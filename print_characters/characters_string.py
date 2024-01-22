def print_even_index_chars():
    user_input = input("Enter a string: ")
    print("Characters at even indices:")

    for i in range(len(user_input)):
        if i % 2 == 0:
            print(f"Index {i}: {user_input[i]}")

print_even_index_chars()
