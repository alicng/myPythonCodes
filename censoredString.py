def uncensor(txt, vowels):
    for i in vowels:
    	txt = txt.replace('*', i, 1)
    return txt

a=uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")
print(a)