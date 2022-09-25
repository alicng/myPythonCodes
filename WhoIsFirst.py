def first_place(road):

    return None if len(road.replace('=','')) == 0 else road.replace('=','')[-1]

a=first_place("==s=h==k=")
print(a)