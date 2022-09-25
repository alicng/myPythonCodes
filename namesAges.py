def organize(txt):
    if len(txt) == 0:
        return {}
    else:
        new_obj = {}
        new_lst = txt.split(',')
        new_obj["name"] = new_lst[0].strip(' ')
        new_obj['age'] = int(new_lst[1].strip(' '))
        new_obj["occupation"] = new_lst[2].strip(' ')
        return new_obj
    
a=organize("John Mayer, 41, Singer")
print(a)