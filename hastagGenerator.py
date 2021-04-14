def generate_hashtag(txt):

    i="#{}".format("".join(txt.title().split()))
    if i=="#" or len(i)>140:
    	return False
    return i

a=generate_hashtag(" " * 100)
print(a)