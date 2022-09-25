def damage(damage, speed, time):

    d={'second':1, 'minute':60, 'hour':3600}
    return "invalid" if damage <0 or speed < 0 else damage * d[time]*speed
    
a=damage(2, 100, "hour")
print(a)