def to_scottish_screaming(txt):

    return ''.join([i.replace(i, 'E') if i in 'aAeEiIoOuU' else i for i in txt.upper() ])

a=to_scottish_screaming("A, wonderful, day, don't, you, think?")
print(a)