 #Find Common Elements in Two Tuples

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))  

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
print(common_elements(tuple1, tuple2))  
