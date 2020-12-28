def convert_to_number(dictionary):

    return {i:int(v) for i, v in dictionary.items()}

a=convert_to_number({ "piano": "200", "tv": "300" })
print(a)