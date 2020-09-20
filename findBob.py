def find_bob(names):

    return -1 if 'Bob' not in names else names.index('Bob')

a=find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"])
print(a)