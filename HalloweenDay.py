def halloween(dt):

    return  "Bonfire toffee" if dt.split('/')[1] == '10' and dt.split('/')[2] == '31' else "toffee"

a=halloween("2013/9/31")
print(a)
#"Bonfire toffee" if dt.split('/')[1] == 10 and dt.split('/')[2] == 31 else "toffee"