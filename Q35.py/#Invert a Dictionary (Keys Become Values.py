#Invert a Dictionary (Keys Become Values, and Values Become Lists of Keys)

def invert_dictionary(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)  
    return inverted

sample_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
print(invert_dictionary(sample_dict))  
