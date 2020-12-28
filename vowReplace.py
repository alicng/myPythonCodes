def vow_replace(word, vowel):
    
    return "".join(vowel if i in 'aeiou' else i for i in word)

a=vow_replace("stuffed jalapeno poppers", "e")
print(a)

#return ''.join([i.replace(i,vowel) if i in 'aeiou' else i for i in word ])