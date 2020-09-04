def find_letters(word):

    
    return [i for i in word if word.count(i) == 1]


a=find_letters("balloon")
print(a)