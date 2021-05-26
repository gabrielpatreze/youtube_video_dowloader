from PIL import Image

#converting image into black an white
img = Image.open("pic2.jpg")

# img.show()

blackAndWhite = img.convert("L")
blackAndWhite.save('pic2_new.jpg')
blackAndWhite.show()

