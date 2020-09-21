def cons(a):
    vowels = 'aeiou'
    for i in range(len(a)-1):
        if a[i] in vowels and a[i+1] in vowels:
            return 'Positive'
    return 'Negative'

user=input('enter a word :')
a=cons(user)
print(a)

