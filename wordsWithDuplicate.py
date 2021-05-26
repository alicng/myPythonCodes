def no_duplicate_letters(phrase):
    
    return all(len(set(i)) == len(i) for i in phrase.split())

a=no_duplicate_letters("So far, so good.")
print(a)
# 