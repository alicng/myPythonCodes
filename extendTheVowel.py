def extend_vowels(word, num):

    return 'invalid' if num < 0 or type(num) == float else ''.join([i*(num+1) if i in 'a,e,i,o,u,E,I,O,U,A' else i for i in word])

a=extend_vowels("Hello", 2)
print(a)