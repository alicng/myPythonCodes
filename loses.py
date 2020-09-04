def calculate_losses(items):

    c=sum(items.values())
    return "Lucky you!" if c==0 else c


a=calculate_losses({
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
})
print(a)