def missing_char(word, n):

    first_part = word[:n]
    second_part = word[n+1:]
    return first_part + second_part

a=missing_char('kitchen', 1)
print(a)