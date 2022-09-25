def bonus(days):

    return 0 if days < 33 else (days - 32)*325 if days < 41 else (8*325)+ (days - 40) * 550 if days < 49 else (8*325)+(8 * 550)+(days-48)*600

a=bonus(50)
print(a)