#Sort a Dictionary Based on Values (Ascending or Descending)

def sort_dict_by_value(d, descending=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=descending))

sample_dict = {"apple": 3, "banana": 1, "cherry": 2}
print(sort_dict_by_value(sample_dict))  
print(sort_dict_by_value(sample_dict, descending=True)) 
