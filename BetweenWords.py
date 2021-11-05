def is_between(first, last, word):

    return first < word < last
    #sorted([first, last, word]) == [first,word,last]
a=is_between("apple", "banana", "azure")
print(a)