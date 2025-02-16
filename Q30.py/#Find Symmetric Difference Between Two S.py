#Find Symmetric Difference Between Two Sets

def symmetric_difference(set1, set2):
    return set1 ^ set2  

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}
print(symmetric_difference(set1, set2))  
