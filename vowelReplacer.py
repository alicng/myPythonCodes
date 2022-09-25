def replace_vowels(txt, ch):
    
    return ''.join([ch if i in 'a,e,i,o,u' else i for i in txt])

a=replace_vowels("the aardvark", "#")
print(a)