"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel_f = figure_img.get_pixel(x, y)
            standard = max(pixel_f.red, pixel_f.blue)
            if pixel_f.green > standard*2:
                pixel_bg = background_img.get_pixel(x, y)
                pixel_f.red = pixel_bg.red
                pixel_f.blue = pixel_bg.blue
                pixel_f.green = pixel_bg.green
    return figure_img


def main():
    """
    This function will photoshop a person with green screen background onto any background.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
