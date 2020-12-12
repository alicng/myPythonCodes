def reverse_words(words):

    return ' '.join(words.split()[::-1])

a=reverse_words("the sky is blue")
print(a)