def reverse_image(image):

    return [[0 if i==1 else 1 for i in j] for j in image]

a=reverse_image([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
])
print(a)