#Implement a code to find the intersection of two given lists

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))  # Find common elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list_intersection(list1, list2))
