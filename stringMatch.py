def str_match_by2char(a, b):
   
    return sum([1 for i in range(len(a)-1) if a[i:i+2] == b[i:i+2]])

a=str_match_by2char("yytaazz", "yyjaaz")
print(a)