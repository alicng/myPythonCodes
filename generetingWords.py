def anagram(name, words):
    
    
    return sorted(''.join(words) + ' ') == sorted(name.lower())
    
a=anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])
print(a)