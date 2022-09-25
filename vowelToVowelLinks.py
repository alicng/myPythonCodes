def vowel_links(txt):

    w, v = txt.split(), 'aeuio'
    return any(w[i][-1] in v and w[i+1][0] in v for i in range(len(w)-1))
    
a=vowel_links("a very large appliance")
print(a)