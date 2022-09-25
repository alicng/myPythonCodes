def censor_string(txt, lst, char):
    
    return ' '.join([i if i not in lst else char * len(i) for i in txt.split()])

a=censor_string("Today is a Wednesday!", ["Today", "a"], "-")
print(a)
#