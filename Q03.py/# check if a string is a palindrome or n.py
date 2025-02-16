# check if a string is a palindrome or not
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]  # Check if the string is equal to its reverse

# Example usage
input_string = "Harshit"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
