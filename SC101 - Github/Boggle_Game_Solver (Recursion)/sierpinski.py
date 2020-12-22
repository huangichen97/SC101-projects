"""
File: sierpinski.py
Name: Ethan
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: This program draws a sierpinski triangle.
	User can manipulate the ORDER constant to change the density of the triangle,
	if the order does not reach zero, the the program will step into the recursive case;
	if reaches zero, then the program will reach the base case and stop drawing.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the number of current triangle; if reach 0, then stop drawing triangles.
	:param length: the side length of the triangle
	:param upper_left_x: the x position of the upper left point of the triangle
	:param upper_left_y: the y position of the upper left point of the triangle
	:return: if 'order' reach zero, then return
	"""
	if order == 0:
		return
	else:

		# draw the triangle
		tri_1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		tri_2 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		tri_3 = GLine(upper_left_x, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		tri_1.color = 'darkslategrey'
		tri_2.color = 'darkslategrey'
		tri_3.color = 'darkslategrey'
		window.add(tri_1)
		window.add(tri_2)
		window.add(tri_3)

		# change the length
		previous_length = length
		length /= 2

		# recursive triangle
		# upper right triangle
		sierpinski_triangle(order-1, length, upper_left_x, upper_left_y)
		# upper left triangle
		sierpinski_triangle(order - 1, length, upper_left_x+previous_length/2, upper_left_y)
		# below triangle
		sierpinski_triangle(order - 1, length, upper_left_x+previous_length/4, upper_left_y+0.866*length)


if __name__ == '__main__':
	main()