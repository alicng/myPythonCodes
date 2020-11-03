def magic(txt):
    if len(str(int(txt[0])*int(txt[2])))==1:
        return int(txt[0])*int(txt[2]) == int(txt[7:])
    elif len(str(int(txt[0])*int(txt[2])))==2:
        return int(txt[0])*int(txt[2]) == int(txt[6:])
    return int(str(txt[0])*int(txt[2])) == int(txt[5:])

a=magic("9 2 2011")
print(a)
#