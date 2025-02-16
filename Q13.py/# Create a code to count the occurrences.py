# Create a code to count the occurrences of each element in a list and return a dictionary with elements 

def count_elements(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

items = [1, 2, 2, 3, 3, 3, 4]
print(count_elements(items))  
