def jay_and_bob(txt):

    d={"half":14, "quarter":7, "eighth":3.5, "sixteenth":1.75}
    return f'{d[txt]} grams'

a=jay_and_bob("eighth")
print(a)