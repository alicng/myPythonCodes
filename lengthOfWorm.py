def worm_length(worm):

    #return "invalid" if set(worm) == {''} or set(worm) != {'-'} else "{} mm.".format(len(worm)*10) 
    return "{} mm.".format(len(worm)*10) if set(worm) == {'-'} else  "invalid"

a= worm_length("---")
print(a)
