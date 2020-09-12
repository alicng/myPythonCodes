def zip_it(women, men):

    return [i for i in zip(women, men)] if len(women) == len(men) else "sizes don't match"

a=zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"])
print(a) 