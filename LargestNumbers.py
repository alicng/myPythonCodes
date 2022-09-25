def largest_numbers(n, lst):

    return [] if n ==0 else sorted(lst)[-n:]

a=largest_numbers(0, [14, 12, 57, 11, 18, 16])
print(a)