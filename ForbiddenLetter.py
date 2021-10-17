def forbidden_letter(char, lst):
    l=list(''.join([i for i in lst]))
    return False if char in l else True
    

a=forbidden_letter("r", ["rock", "paper", "scissors"])
print(a)