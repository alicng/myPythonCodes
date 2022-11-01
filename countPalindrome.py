def count_palindromes(num1, num2):
    
    
    return len([1 for i in range(num1, num2 +1) if str(i) == str(i)[::-1]])

a=count_palindromes(1,10)
print(a)