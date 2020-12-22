"""
File: shrink.py
-------------------------------
This program creates a new "out" image half
the width and height of the original.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    This function shrinks the original image.
    ----------------------------------------------------------
    :param filename:str, the file path of the original image.
    :return SimpleImage, the shrunk image.
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            new_pixel = new_img.get_pixel(x, y)
            pixel1 = img.get_pixel(x*2, y*2)
            pixel2 = img.get_pixel(x*2, y*2 + 1)
            pixel3 = img.get_pixel(x*2 + 1, y*2)
            pixel4 = img.get_pixel(x*2 + 1, y*2 + 1)
            new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
            new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
            new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4
    return new_img


def main():
    """
    Input 'Poppy.png' and create a new image
    half the width and height of the original.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
