"""
File: draw_line
Name:Ethan Huang
-------------------------
TODO:
This program opens a canvas and draws circles and lines in the following steps:

First, it detect if the click is a "first click" or a "second click".

If first click, the program will draw a hollow circle by SIZE.
If second click, the it will create a line from the circle to the new click,
and also delete the circle and then start a new round.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

is_first = True
circle_x = 0
circle_y = 0
circle = 0

window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global is_first, circle, circle_x, circle_y

    if is_first is True:
        # The click is a first click(1st, 3th, 5th, etc.)
        # Should draw a circle on the mouse click
        circle = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        window.add(circle)
        is_first = False  # To make the next click a second click
        circle_x = mouse.x - SIZE / 2
        circle_y = mouse.y - SIZE / 2

    else:
        # The click is a second click(2nd, 4th, 6th, etc.)
        # Should draw a line from the circle(created by the first click) to the new click
        window.remove(circle)
        the_line = GLine(circle_x, circle_y, mouse.x, mouse.y)
        window.add(the_line)
        is_first = True  # To make the next click a first click again


if __name__ == "__main__":
    main()
