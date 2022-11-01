def camel_to_snake(s):
    
    return ''.join(['_' + i.lower() if i.isupper() else i for i in s])

a=camel_to_snake("greatApples for aSmellyRhino")
print(a)