def remove_vowels(txt):
    
    return ''.join([i for i in txt.lower() if i not in ['a','e','i','u','o']])
    #return ''.join(char for char in txt if not char in "aeiouAEIOU")

a=remove_vowels("If Obama resigns from office NOW, thereby doing a great service to the country - I will give him free lifetime golf at any one of my courses!")
print(a)

