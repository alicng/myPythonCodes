def jazzify(lst):

    return [i+'7' if '7' not in i else i for i in lst ]

a=jazzify(['G', 'C7'])
print(a)