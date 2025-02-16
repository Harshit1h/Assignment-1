#Find Intersection of Two User-Input Sets

def intersection_of_sets():
    set1 = set(map(int, input("Enter first set of numbers separated by commas: ").split(",")))
    set2 = set(map(int, input("Enter second set of numbers separated by commas: ").split(",")))
    return set1 & set2 

print(intersection_of_sets())

