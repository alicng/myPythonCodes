def word_builder(ltr, pos):
    
        return ''.join([ltr[i] for i in pos])

a=word_builder(["e", "t", "s", "t"], [3, 0, 2, 1])
print(a)
