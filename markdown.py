def md_format(word, style):
    d = {"b":"**", "i":"_","c":"`","s":"~~"}
    return d[style] + word + d[style]
 
a=md_format("That's a strike!", "s")
print(a)