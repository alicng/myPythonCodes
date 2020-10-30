def construct_fence(p):

    return (1000000//int(p[1:].replace(',', '')))*'H'

a=construct_fence("$100,000")
print(a)