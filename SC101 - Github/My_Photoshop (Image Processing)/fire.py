"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.2


def main():
    """
    This program will highlight the fired area with burning red(R=225, G=0, B=0),
    and paint other area into grey scale.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    This function highlights the fire spots.
    ----------------------------------------------------------
    :param filename:str, the file path of the original image.
    :return image: The image with highlighted fire.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.green+pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 225
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


if __name__ == '__main__':
    main()
