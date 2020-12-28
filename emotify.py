def emotify(txt):
    d={'smile':':D', 'grin':':)', 'sad':':(', 'mad':':P'}
    return ' '.join(txt.split()[:-1])+' '+d[''.join(txt.split()[-1])]

a=emotify("Make me smile")
print(a)
