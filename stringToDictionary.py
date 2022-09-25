def str_to_dict(lst):
    
    return dict(i.split('=') for i in lst)
    # {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    # {k:v for (k,v) in map(lambda x: x.split('='),l)}
a=str_to_dict(["1=one", "2=two", "3=three", "4=four"])
print(a)