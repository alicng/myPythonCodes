def three_letter_collection(s):

    return [s[i:i+3] for i in range(len(s)-2)]
    
a=three_letter_collection("click")
print(a)