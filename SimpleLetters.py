def longest_string(str1, str2):
    
    return ''.join(sorted(set(str1+str2)))

a=longest_string("lordsofthefallen", "gamekult")
print(a)