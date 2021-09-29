def check_title(txt):

    return all([i[0].isupper() for i in txt.split()])

a=check_title("A Mind boggling Achievement")
print(a)