def relation_to_luke(name):
    d={'Darth Vader':'father','Leia':'sister','Han':'brother in law','R2D2':'droid'}
    
    return  "Luke, I am your {}.".format(d[name])

a=relation_to_luke("Darth Vader")
print(a)