"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str, the file path of the original image.
    :return img: The image that is vertical-mirrored.
    """
    img = SimpleImage(filename)
    img_blank = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            old_pixel = img.get_pixel(x, y)
            new_pixel1 = img_blank.get_pixel(x, y)
            new_pixel2 = img_blank.get_pixel(x, img_blank.height-1-y)

            new_pixel1.red = old_pixel.red
            new_pixel1.green = old_pixel.green
            new_pixel1.blue = old_pixel.blue

            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue

    return img_blank


def main():
    """
    This program makes a vertical-mirrored image of mt-rainier.jpg by
    inserting old pixels into the blank new canvas.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
