#Find Elements in First Set but Not in Second

def difference_of_sets():
    set1 = set(input("Enter first set of strings separated by commas: ").split(","))
    set2 = set(input("Enter second set of strings separated by commas: ").split(","))
    return set1 - set2  

print(difference_of_sets())
