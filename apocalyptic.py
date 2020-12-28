def apocalyptic(n):

    num=str(2**n)
    return "Repent! {} days until the Apocalypse!".format(num.index('666'))if '666' in num else "Crisis averted. Resume sinning."

a=apocalyptic(175)
print(a)