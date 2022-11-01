def organize(txt):
    try:
        y={}
        x=[i for i in txt.split(',')]
        y["name"] = x[0].strip(' ')
        y["age"] = int(x[1].strip(' '))
        y["occupation"] = x[2].strip(' ')
    except:
        return {}
    return y

    # txt = txt.split(",")
	# return {"age":int(txt[1]),"occupation":txt[2].strip(" "),"name":txt[0]}
a=organize("John Mayer, 41, Singer")
print(a)

