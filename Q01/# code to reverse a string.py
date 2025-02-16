# code to reverse a string
def reverse_string(s):
    return s[::-1]  # Using slicing to reverse the string

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(f"Original: {original_string}")
print(f"Reversed: {reversed_string}")
