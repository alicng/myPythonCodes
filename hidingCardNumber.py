def card_hide(card):
    
    return (len(card)-5)*'*'+card.replace(card[:-4],'*')
    #return '*'*len(card[:-4])+card[-4:]

a=card_hide("1234123456785678")
print(a)