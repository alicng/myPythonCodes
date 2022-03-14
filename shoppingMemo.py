def checkout(cart):
    
    
    return sum(i['prc']*i['qty']*(1.06 if i['taxable'] else 1) for i in cart)

a=checkout([
  { "desc": "potato chips", "prc": 2, "qty": 2, "taxable": False },
  { "desc": "soda", "prc": 3, "qty": 2, "taxable": False },
  { "desc": "paper plates", "prc": 5, "qty": 1, "taxable": True }
]) 
print(a)