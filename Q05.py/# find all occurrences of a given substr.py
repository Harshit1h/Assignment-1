# find all occurrences of a given substring within another string

def find_substring_occurrences(main_string, substring):
    # List to store the starting indices of the substring occurrences
    indices = []
    
    # Start at the beginning of the main string
    start = 0
    
    # Loop to find all occurrences of the substring
    while start < len(main_string):
        # Find the substring starting from the current position
        index = main_string.find(substring, start)
        
        # If no more occurrences are found, break the loop
        if index == -1:
            break
        
        # Add the index to the list
        indices.append(index)
        
        # Move the start position to just after the current found substring
        start = index + 1
    
    return indices

main_string = "This is a simple example. This example is simple."
substring = "simple"
indices = find_substring_occurrences(main_string, substring)

print(f"Occurrences of '{substring}' found at indices: {indices}")
