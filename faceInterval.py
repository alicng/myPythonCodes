def face_interval(num):

    dff=max(num)-min(num)
    return ":/" if type(num) is not list else ":)" if dff in num else ":("

a=face_interval([5, 2, 8, 3, 11])
print(a)