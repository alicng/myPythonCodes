def unique_styles(albums):


    return len(set(','.join(albums).split(',')))

a=unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
])
print(a)