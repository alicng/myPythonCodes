def alphabet_index(alphabet, string):
      
    x=sorted([((ord(i.lower()))) for i in string])[-1]
    return '{}{}'.format(x-96,chr(x))
    """
alphabet = []
def alphabet_index(*args):
    res, max_idx = "a", 97
    for c in args[1].lower():
        idx = ord(c)
        if idx > max_idx:
            res = "{}{}".format(idx - 96, c)
            max_idx = idx
    return res
    """

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
a=alphabet_index(alphabet, "Rogei")
print(a)