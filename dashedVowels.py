def dashed(txt):
    
    return ''.join(['-{}-'.format(i) if i.lower() in'aeiou' else i for i in txt ])

a=dashed("Carpe Diem")
print(a)