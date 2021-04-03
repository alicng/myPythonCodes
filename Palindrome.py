def is_palindrome(word):

    return word[::]==word[::-1]

a=is_palindrome("boob")
print(a)