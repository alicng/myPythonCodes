def longest_time(h, m, s):

    return max((h*3600, h), (m*60, m), (s, s))
a=longest_time(5, 233, 999)
print(a)
#return h if h*3600 > m * 60 and h*3600 > s else m if m * 60 > h*3600 and m * 60 >s else s
