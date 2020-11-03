def index_filter(indexes, string):

    return ''.join([string.lower()[i] for i in indexes])

a=index_filter([0, 1, 5, 7, 4, 2], "Cry me a river")
print(a)
#