def valid(txt):

    return len(txt)==4 or len(txt)==6 and txt.isdigit() and ' ' not in txt 

a=valid("y1356")
print(a)
#len(txt) in [4,6] and txt.isdigit()