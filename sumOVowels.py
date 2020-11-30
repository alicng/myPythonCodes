def sum_of_vowels(sentence):

    d={'A':4, "E":3, "I":1, "O":0, "U":0}
    return sum([d[i] for i in sentence.upper() if i in 'AEIOU'])

a=sum_of_vowels("Do I get the correct output?")
print(a)