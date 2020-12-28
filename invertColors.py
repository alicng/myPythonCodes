def color_invert(rgb):

    return tuple([255-i for i in rgb])

a=color_invert((165, 170, 221))
print(a)