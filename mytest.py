def mytest(n):
    
    vowel_counts = {}

    for vowel in "aeiou":
        count = lowercase.count(vowel)

        vowel_counts[vowel] = count
    print(vowel_counts)

a=mytest('there is a cat in the box and umbrella tox')
print(a)