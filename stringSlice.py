
def slic(a):
    '''
    txt = "abcdefghijklmnopqrstuvwxyz"
    challenge1(txt) ➞ "abcde"
    # First 5 characters of the string.

    challenge2(txt) ➞ "vwxyz"
    # Last 5 characters of the string.

    challenge3(txt) ➞ "zyxwvutsrqponmlkjihgfedcba"
    # All characters in the string from back.

    challenge4(txt) ➞ "fedcba"
    # First 6 characters in the string (start with 6th character).

    challenge5(txt) ➞ "tvxz"
    # Take last 7 characters and only return odd positioned ones.
    '''
    def challenge1(s):
    	return s[:5]

def challenge2(s):
	return s[-5:]

def challenge3(s):
	return s[::-1]

def challenge4(s):
	return s[5::-1]

def challenge5(s):
	return s[-7::2]

a=slic("0123456789")
print(a)
