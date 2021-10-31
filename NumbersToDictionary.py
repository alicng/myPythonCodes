def num_to_dict(lst):

    return [{str(i) : chr(i)} for i in lst]

a=num_to_dict([118, 117, 120])
print(a)