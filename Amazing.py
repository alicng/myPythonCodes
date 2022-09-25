def amazing_edabit(s):

    return ' '.join(s.split()[0:2]) +" "+'not'+' '+ 'amazing' if 'edabit' not in s else s

a=amazing_edabit("edabit is amazing.")
print(a)