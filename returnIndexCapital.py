def index_of_caps(word):
    
    return [word.index(i)  for i in word if i.isupper()]

a=index_of_caps("eQuINoX")
print(a)