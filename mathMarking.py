def mark_maths(lst):
    a=[eval((i.split('='))[0])==int((i.split('='))[1]) for i in lst]
    return '{}%'.format(round((a.count(True)/len(a))*100))
a=mark_maths(["2+3=5", "4+4=9", "3-1=2"])
print(a)
# 