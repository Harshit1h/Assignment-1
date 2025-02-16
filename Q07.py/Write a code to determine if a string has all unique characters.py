# Write a code to determine if a string has all unique characters 

def has_unique_chars(s):
    return len(set(s)) == len(s)  

print(has_unique_chars("abcdef"))  

print(has_unique_chars("hello"))   
