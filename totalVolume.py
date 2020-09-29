def total_volume(*boxes):

    return  sum([x*y*z for x,y,z in boxes])


a=total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1])
print(a)