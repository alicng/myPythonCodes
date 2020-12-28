def longest_word(s):

    
    return max(s.split(), key=len)
  

a=longest_word("Forgetfulness is by all means powerless!")
print(a)
#