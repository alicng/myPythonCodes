def reverse(dct):
    
    return dict(zip(dct.values(), dct.keys()))
    #{v: k for k, v in dct.items()}

a=reverse({"boy": "ragazzo", "girl": "ragazza", "baby": "bambino"})
print(a)