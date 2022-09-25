def fruit_salad(fruits):
    t=[i[0:(len(i)//2)] for i in fruits]
    x=[x[(len(x)//2):] for x in fruits]
    return ''.join(sorted(t + x))

a=fruit_salad(["apple", "pear", "grapes"])
print(a)