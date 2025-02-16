#Count Word Frequencies in a List

def word_frequencies(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

word_list = ["apple", "banana", "apple", "cherry", "banana", "banana"]
print(word_frequencies(word_list))  

