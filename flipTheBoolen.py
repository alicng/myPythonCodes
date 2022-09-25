def reverse(arg):
    
    return "boolean expected" if type(arg) is not bool else not arg  
    #return not arg if isinstance(arg, bool) else "boolean expected"
a=reverse(True)
print(a)