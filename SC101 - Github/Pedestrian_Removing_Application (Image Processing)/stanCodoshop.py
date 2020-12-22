"""
File: stanCodoshop.py
Name: Ethan Huang
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------

TODO:
This program finds the best pixel from all the pictures provided,
and generate a final picture without people.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red) ** 2 + (green-pixel.green) ** 2 + (blue-pixel.blue) ** 2) ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    rgb = []
    pix_red_sum = 0
    pix_green_sum = 0
    pix_blue_sum = 0

    for i in range(len(pixels)):
        pixel = pixels[i]
        pix_red_sum += pixel.red
        pix_green_sum += pixel.green
        pix_blue_sum += pixel.blue

    rgb.append(pix_red_sum//i)
    rgb.append(pix_green_sum//i)
    rgb.append(pix_blue_sum//i)

    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb_avg = get_average(pixels)
    red_avg = rgb_avg[0]
    green_avg = rgb_avg[1]
    blue_avg = rgb_avg[2]

    for i in range(len(pixels)):
        pixel = pixels[i]
        dist = get_pixel_dist(pixel, red_avg, green_avg, blue_avg)
        if i == 0:
            best_pix = pixel
            shortest = dist
        else:
            if dist < shortest:
                best_pix = pixels[i]
                shortest = dist
            else:
                pass

    return best_pix


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):

            # To get the correct pixel of the pictures and result
            result_pix = result.get_pixel(x, y)

            # Creates a list and store pixels from each picture
            pixels = []
            for k in range(len(images)):
                pixels.append(images[k].get_pixel(x, y))

            # Returns the best pixel
            best_pixel = get_best_pixel(pixels)

            # Puts the best pixel onto the result canvas
            result_pix.red = best_pixel.red
            result_pix.green = best_pixel.green
            result_pix.blue = best_pixel.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
