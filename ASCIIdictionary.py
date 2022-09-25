def to_dict(lst):
    
    return [{i:ord(i)} for i in lst]

a=to_dict(["^", "b", "c"])
print(a)