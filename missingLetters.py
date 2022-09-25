def get_missing_letters(s):
    
    alp="abcdefghijklmnopqrstuvwxyz"
    return ''.join([i for i in alp if i not in s])
 
a=get_missing_letters("abcdefgpqrstuvwxyz")
print(a)