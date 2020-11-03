def replace_vowel(word):

    d={'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
    
    return "".join([i if i not in d else d[i] for i in word])

a=replace_vowel("washington")
print(a)
#return word.translate(str.maketrans('aeiou', '12345'))