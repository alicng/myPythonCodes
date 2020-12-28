def valid_division(d):
    try:
        return round(eval(d))==eval(d)
    except:
        return "invalid"

a=valid_division("30/25")
print(a)