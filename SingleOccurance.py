import collections
def single_occurrence(txt):
    
    return "".join([i for i in txt.upper() if txt.upper().count(i) == 1])

a=single_occurrence("AAAAVNNNNSS")
print(a)