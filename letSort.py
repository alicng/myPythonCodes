def asc_des_none(lst, s):

    d={'Asc':sorted(lst), 'Des':lst[::-1], 'None':lst[::]}
    return d[s]

a=asc_des_none([4, 3, 2, 1], "None" )
print(a)
#return sorted(lst, reverse=s == 'Des') if s else lst