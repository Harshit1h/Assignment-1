#Merge Two Dictionaries, Adding Values for Common Keys

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value  
    return merged


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
print(merge_dictionaries(dict1, dict2))  
