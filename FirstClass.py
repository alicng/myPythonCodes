def determine_lever(l):
    lever = 'first' if l[1]=='f' else 'second' if l[1]=='l' else 'third'
    return '{} class lever'.format(lever)

a=determine_lever(["e", "l", "f"])
print(a)