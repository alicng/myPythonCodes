words1 = ["you","much","hard"]
words2 = ["i","you","he"]
words3 = ["love","ate","works"]

print ([i for i in (list(map(lambda x, y, z : x+' '+y+' '+z, words2, words3, words1)))])