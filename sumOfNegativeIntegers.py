def negative_sum(chars):

    chars = ''.join([i if i.isdigit() else ' -' if i=='-' else ' ' for i in chars]).split()
    print(chars)
    return sum([int(i) for i in chars if int(i)<0])

a=negative_sum("22 13%14&-11-22 13 12")
print(a)
    