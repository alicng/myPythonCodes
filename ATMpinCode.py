def is_valid_PIN(pin):
    
    return pin.isdigit() and len(pin) == 4 or len(pin) == 6 

a=is_valid_PIN("12346")
print(a)