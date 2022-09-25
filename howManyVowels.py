def count_vowels(txt):
    
    return sum([len(i) for i in txt if i in 'a,e,i,o,u'])

a=count_vowels("Celebration")
print(a)