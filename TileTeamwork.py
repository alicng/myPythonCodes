def possible_bonus(a, b):

    return True if b-a < 7 and b-a > 0 else False
    #return 0 < b-a <= 6

a=possible_bonus(8, 7)
print(a)