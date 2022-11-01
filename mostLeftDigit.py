from curses.ascii import isdigit


def left_digit(num):
    
    return [int(i) for i in num if i.isdigit()][0]

a=left_digit("TrAdE2W1n95!")
print(a)