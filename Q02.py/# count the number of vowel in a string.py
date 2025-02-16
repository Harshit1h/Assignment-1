# count the number of vowel in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"  
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print(f"Number of vowels in '{input_string}': {vowel_count}")
