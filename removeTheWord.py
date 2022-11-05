def remove_letters(letters, word):
    [letters.remove(i) for i in word if i in letters]
    return letters
    

a=remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon")
print(a)