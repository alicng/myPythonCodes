def get_drink_ID(flavor, ml):

    
    return '{}{}'.format (''.join(i[:3].upper() for i in flavor.split()), ml.strip('ml'))

a=get_drink_ID("passion fruit", "750ml")
print(a)
#