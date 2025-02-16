# Merge Two Sorted Lists Into a Single Sorted List

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)  # Merge and sort

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))  

