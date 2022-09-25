def get_type(value):

    return type(value).__name__

a=get_type([])
print(a)