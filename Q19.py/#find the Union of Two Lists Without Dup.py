#find the Union of Two Lists Without Duplicates
def list_union(lst1, lst2):
    return list(set(lst1) | set(lst2))  # Merge and remove duplicates

list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(list_union(list1, list2))  
