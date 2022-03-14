def solve(eq):
    if eq[2] == '+' and eq.split()[-1] > eq.split()[-3]:
      return abs(eval(eq.replace('=', '-')[3:]))
    elif eq[2] == '+' and eq.split()[-1] < eq.split()[-3]:
      return -(eval(eq.replace('=', '-')[3:]))
    else:
        return (eval(eq.replace('=', '+')[3:]))
    #return -eval(eq[1:].replace("=", "-"))
a=solve("x + -500 = -200")
print(a)