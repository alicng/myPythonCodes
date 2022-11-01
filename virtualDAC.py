def V_DAC(value):
    
    return round(5*value/1023, 2)

a=V_DAC(400)
print(a)