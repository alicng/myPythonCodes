import math
def century_from_year(year):
    if len(str(year)) < 4:
        return str(year)[0:1] if str(year)[-2:] == "00" else int(str(year)[0:1])+1
    return str(year)[0:2] if str(year)[-2:] == "00" else int(str(year)[0:2])+1
    
a=century_from_year(201)
print(a)