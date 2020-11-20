def fifth(*args):
    return type(args[4]) if len(args) >= 5 else "Not enough arguments"
a=fifth("a", 2, 3, [1, 2, 3], "five")
print(a)