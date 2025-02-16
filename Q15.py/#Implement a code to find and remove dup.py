 #Implement a code to find and remove duplicates from a list while preserving the original order of 

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  
