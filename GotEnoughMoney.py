def items_purchase(store, wallet):
    
    afford = sorted(k for k, j in store.items()
                 if int(j[1:].replace(',', '')) <= int(wallet[1:]))
    return afford if afford else "Nothing"

a=items_purchase({
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}, "$300")
print(a)

