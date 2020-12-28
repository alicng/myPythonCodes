def dolla_dolla_bills(money):


    return '${:,.2f}'.format(money).replace('$-', '-$')

a=dolla_dolla_bills(-314159.2653)
print(a)