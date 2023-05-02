# graph = [[1, 4], [1, 3], [2, 6], [2, 4]]
# graph.sort(key=lambda x: x[1])
# print(graph)

from PIL import Image

# open image file
image = Image.open("C:/Users/intern/Downloads/ddd.jpg")

# resize image to 140x180 pixels
resized_image = image.resize((3900, 3900))

# save resized image to file
resized_image.save("C:/Users/intern/Downloads/hi.jpg")