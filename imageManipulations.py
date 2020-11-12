from PIL import Image
import numpy as np
import math
import imageio

def Atest() :
    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    #img = Image.new( 'RGB', (250,250), "black") # create a new black image
    img = Image.open(r"images/benImage.jpg")
    pixels = img.load() # create the pixel map

    print("img.size[0] : ", img.size[0])
    print("img.size[1] : ", img.size[1])
    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            R = int(pixels[i,j][0]*0.1)
            G = pixels[i,j][1]
            B = pixels[i,j][2]
            pixels[i, j] = (R, G, B)  # set the colour accordingly

    img.show()

def create_image(i, j):
    # create a new black image
    # can be changed to "black"
  image = Image.new("RGB", (i, j), "white")
  return image

def grayScaleImage() :
    img = Image.open(r"images/benImage.jpg")
    width, height = img.size
    new = create_image(width, height)

    pixels = new.load()
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = img.getpixel((i, j))
            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            # Transform to grayscale
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    new.show()
    new.save('temp.png')

def tryNumpy() :
    img = Image.open(r"images/benImage.jpg")
    imgArray = np.asarray(img)
    width, height = img.size
    print((width, height))
    print(np.shape(imgArray))
    width, height, color = np.shape(imgArray)
    print("w, h, p : ", (width, height, color))
    for x in range(width) :
        for y in range(height) :
            temp_pixel = imgArray[x, y]
            R = temp_pixel[0]
            G = temp_pixel[1]
            B = temp_pixel[2]

            gray = (R * 0.299) + (G * 0.587) + (B * 0.114)
            #imgArray[x, y] = [gray, gray, gray]
            if x == 2 and y == 2:
                print(temp_pixel)


# read an image
image = imageio.imread('images/benImage.jpg')
width, height, color = image.shape
print(type(image))
for x in range(width):
    for y in range(height):
        temp = image[x,y]