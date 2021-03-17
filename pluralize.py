def pluralize(lst):

    return {i+'s' if lst.count(i) > 1 else i for i in lst }

a=pluralize(["cow", "pig", "cow", "cow"])
print(a)