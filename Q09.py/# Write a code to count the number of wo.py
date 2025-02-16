# Write a code to count the number of words in a string

def count_words(s):
    return len(s.split())  

sentence = "Python is a great programming language"
print(count_words(sentence))  
