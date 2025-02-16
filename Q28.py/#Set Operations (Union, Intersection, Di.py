#Set Operations (Union, Intersection, Difference)
def set_operations(set1, set2):
    return {
        "Union": set1 | set2,
        "Intersection": set1 & set2,
        "Difference": set1 - set2
    }

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set_operations(set1, set2))

