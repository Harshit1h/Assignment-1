# Write a code to perform basic string compression using the counts of repeated character

def compress_string(input_string):
    compressed = []
    
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1 
             # Increment count for consecutive characters
        else:
            # Append the character and its count to the result
            compressed.append(input_string[i - 1] + str(count))
            count = 1  # Reset count for the next character
    
    # Append the last character and its count
    compressed.append(input_string[-1] + str(count))
    
    # Join the list into a single string and return it
    compressed_string = ''.join(compressed)
    
    # If the compressed string is longer than the original, return the original string
    return compressed_string if len(compressed_string) < len(input_string) else input_string

input_string = "aabcccccaaa"
compressed = compress_string(input_string)

print(f"Original string: {input_string}")
print(f"Compressed string: {compressed}")
