# Write a code to remove all occurrences of a specific element from a list

def remove_occurrences(lst, element):
    return [x for x in lst if x != element]

numbers = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2
print(remove_occurrences(numbers, element_to_remove))  
