#Access a Value in a Nested Dictionary Using a List of Keys

def get_nested_value(d, keys):
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]  
        else:
            return None  
    return d  

nested_dict = {"a": {"b": {"c": 42}}}
key_list = ["a", "b", "c"]
print(get_nested_value(nested_dict, key_list))  
print(get_nested_value(nested_dict, ["a", "x", "c"]))  

