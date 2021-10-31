def filter_string(txt):
    u = sum(1 for i in txt if i.isupper())
    l = sum(1 for i in txt if i.islower())
    n = sum(1 for i in txt if i.isdigit())
    s = sum(1 for i in txt if not i.isalnum())
    
    return [u, l, n, s]
    
a=filter_string("*$(#Tu12baS43tkR%@*!")
print(a)
# Create a function which takes a string txt and returns a list of 
# numbers with count of uppercase letters, lowercase letters, 
# numbers and special characters.