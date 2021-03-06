def neighboring(txt):

    return all(abs(ord(a) - ord(b)) == 1 for a, b in zip(txt, txt[1:]))

a=neighboring("abcdedcba")
print(a)
'''
Create a function that takes a string and checks if every single character 
is preceded and followed by a character adjacent to it in the english alphabet.

Example: "b" should be preceded and followed by ether "a" or "c" 
(abc || cba || aba || cbc == True but abf || zbc == False).
'''