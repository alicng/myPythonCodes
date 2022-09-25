def even_odd_string(txt):
    
    return f'{txt[0::2]} {txt[1::2]}'

a=even_odd_string("airforce")
print(a)
# even-indexed and odd-indexed characters are grouped and groups are space-separated.