def front_back(word):

    word1=word.replace(word[0], word[-1])
    return word1[:-1]+word[0]

a=front_back('clarusway')
print(a)