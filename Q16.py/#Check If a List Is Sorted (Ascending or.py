#Check If a List Is Sorted (Ascending or Descending)

def is_sorted(lst):
    if lst == sorted(lst):
        return "Ascending"
    elif lst == sorted(lst, reverse=True):
        return "Descending"
    else:
        return "Not sorted"

numbers = [1, 2, 3, 4, 5]
print(is_sorted(numbers))  
