def is_vowel_sandwich(s):

    v='a,e,i,o,u'
    return False if len(s) > 3 else s[0] not in v and s[-1] not in v and s[1] in v


a=is_vowel_sandwich("cab")
print(a)
