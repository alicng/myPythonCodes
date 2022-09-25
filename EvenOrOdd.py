def even_or_odd(s):
    num=[int(str(i)) for i in s]
    odd=sum([i for i in num if i % 2])>sum([i for i in num if i % 2 ==0])
    even= sum([i for i in num if i % 2])<sum([i for i in num if i % 2 ==0])
    return "Odd is greater than Even" if odd is True else "Even is greater than Odd" if even is True else "Even and Odd are the same"
    
a=even_or_odd("12345")
print(a)