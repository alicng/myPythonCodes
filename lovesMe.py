def loves_me(n):
    word = ["Loves me" if i % 2 == 0 else "Loves me not" for i in range(0, n)]
    word[-1] = word[-1].upper()
    return ', '.join(word)
a=loves_me(6)
print(a)
