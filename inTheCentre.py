def is_central(txt):

    return txt == txt[::-1]
    
a=is_central('   G     ')
print(a)
#mid = len(txt)//2
	#return txt[mid] != ' ' if len(txt) % 2 ==  1 else False