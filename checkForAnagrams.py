def is_anagram(s1, s2):
    
    return sorted(s1.lower())==sorted(s2.lower())

a=is_anagram("cristian", "Cristina")
print(a)