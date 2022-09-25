import math
def get_number_of_js(n, p):
    j=math.floor(n-(n*int(p.replace('%', ''))/100))
    return  j if j > 0 else "The children didn't get any apples"

a=get_number_of_js(10, "44%")
print(a)