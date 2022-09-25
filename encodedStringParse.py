def parse_code(txt):

    n, s, x = [i for i in txt.split('0') if len(i)]
    return {'first_name': n, 'last_name': s, 'id': x}

a=parse_code("John000Doe000123")
print(a)
