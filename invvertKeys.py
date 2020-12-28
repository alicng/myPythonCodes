def invert(dct):

    return {dct[i]:i for i in dct}

a=invert({ "zebra": "koala", "horse": "camel" })
print(a)
#dict(zip(dct.values(), dct.keys()))
#{v: k for k, v in d.items()}