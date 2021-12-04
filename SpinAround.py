def spin_around(lst):
    d={"left":-90, "right":90}
    return abs(sum([d[i] for i in lst]) // 360)

a=spin_around(['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'])
print(a)

# Given a list of directions to spin, "left" or "right", 
# return an integer of how many full 360° rotations were made. 
# Note that each word in the list counts as a 90° rotation in that direction.