def error(n):
    d={1:"Check the fan", 2:"Emergency stop", 3:"Pump Error", 4:"c", 5:"Temperature Sensor Error"}
    return 101 if n not in d.keys() else '{}: e{}'.format(d[n],n)

a=error(1)
print(a)