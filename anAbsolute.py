def absolute(txt):
    
    return ' '.join([i.replace(i,i+'n absolute') if i in 'a,A' else i for i in txt.split() ])

a=absolute("I am a champion!!!")
print(a)