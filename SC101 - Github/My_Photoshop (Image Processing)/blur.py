"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: The image that will be blurred.
    :return: new_img: The blurred image.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            if x == 0 and y == 0:
                # Top-left corner.
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red)//4
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green)//4
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue)//4

            elif x == img.width - 1 and y == 0:
                # Top-right corner.
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x - 1, y + 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4

            elif x == 0 and y == img.height - 1:
                # Bottom-left corner
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x + 1, y - 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4

            elif x == img.width - 1 and y == img.height - 1:
                # Bottom-right corner
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x - 1, y - 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4

            elif y == 0 and 0 < x < img.width - 1:
                # First row
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x + 1, y + 1)
                pixel5 = img.get_pixel(x-1, y)
                pixel6 = img.get_pixel(x-1, y+1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6

            elif y == img.height - 1 and 0 < x < img.width - 1:
                # Last row
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x + 1, y - 1)
                pixel5 = img.get_pixel(x - 1, y)
                pixel6 = img.get_pixel(x - 1, y - 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6

            elif x == 0 and 0 < y < img.height - 1:
                # First column
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y+1)
                pixel3 = img.get_pixel(x, y-1)
                pixel4 = img.get_pixel(x + 1, y)
                pixel5 = img.get_pixel(x + 1, y+1)
                pixel6 = img.get_pixel(x + 1, y-1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6

            elif x == img.width - 1 and 0 < y < img.height - 1:
                # Last column
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y + 1)
                pixel3 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel5 = img.get_pixel(x - 1, y + 1)
                pixel6 = img.get_pixel(x - 1, y - 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6

            else:
                # Inner pixels.
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y + 1)
                pixel3 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel5 = img.get_pixel(x - 1, y + 1)
                pixel6 = img.get_pixel(x - 1, y - 1)
                pixel7 = img.get_pixel(x + 1, y)
                pixel8 = img.get_pixel(x + 1, y - 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red + pixel7.red + pixel8.red + pixel9.red) // 9
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green + pixel7.green + pixel8.green + pixel9.green) // 9
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue + pixel7.blue + pixel8.blue + pixel9.blue) // 9

    return new_img


def main():
    """
    This program shows the original image(smiley-face.png) first,
    and then blurs the original image into blurred_img.
    Users can adjust how blur they want the image to be.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    times = int(input('How Blur? (From 1-10): '))
    blurred_img = blur(old_img)
    for i in range(times-1):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
