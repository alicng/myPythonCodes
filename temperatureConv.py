def temp_conversion(celsius):
    F=celsius*9/5 +32
    K=celsius + 273.15
    return "Invalid" if K < 0 else [F, K]
    

a=temp_conversion(-273.16)
print(a)