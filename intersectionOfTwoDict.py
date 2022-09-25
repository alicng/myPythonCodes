def intersection(h1, h2):
    
    a = {k: v for k, v in h1.items() if k in h2}
    b = {k: v for k, v in h2.items() if k in h1}
    return [a, b]
    
dict1 = {"a": 5, "b": 13, "c": 7}
dict2 = {"b": 5, "c": 8, "d": 91, "e": 99}
dict3 = {"a": 1, "b": 34}
dict4 = {"c": 9, "d": 8}    
a=intersection(dict1, dict2)
print(a)