def word_nest(word, nest):

    return len(nest) // len(word) - 1

a=word_nest("code", "cocodccococodededeodeede")
print(a) 