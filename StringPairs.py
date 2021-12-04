def string_pairs(s):
    ss=[s[i]+s[i+1] for i in range(0, len(s)-1, 2)]
    return ss if len(s)%2==0 else ss+[s[-1]+'*']

a=string_pairs("airforces")
print(a)