# Implement a code to find the second largest number in a given list of integers

def second_largest(lst):
    unique_numbers = list(set(lst))  
    if len(unique_numbers) < 2:
        return None  
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]  

numbers = [10, 20, 4, 45, 99, 45]
print(second_largest(numbers))  
