def secret(text):

    return "<{}></{}>".format(text.split("*")[0],text.split("*")[0])*int(text.split("*")[-1])

a=secret("div*2")
print(a)
# "{}*{}".format(text.split("*")[0],int(text.split("*")[-1]))