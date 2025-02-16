# Find the Union of Two Sets of Characters
def union_of_sets():
    set1 = set(input("Enter first set of characters separated by commas: ").split(","))
    set2 = set(input("Enter second set of characters separated by commas: ").split(","))
    return set1 | set2  
print(union_of_sets())
