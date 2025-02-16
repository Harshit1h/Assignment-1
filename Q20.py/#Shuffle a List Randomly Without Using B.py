#Shuffle a List Randomly Without Using Built-in shuffle
import random

def shuffle_list(lst):
    shuffled = lst[:]
    for i in range(len(shuffled)):
        j = random.randint(0, len(shuffled) - 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]  
    return shuffled

numbers = [1, 2, 3, 4, 5]
print(shuffle_list(numbers))  
