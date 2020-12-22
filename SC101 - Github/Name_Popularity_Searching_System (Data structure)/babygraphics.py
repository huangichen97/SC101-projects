"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

NAME: Ethan Huang

This program creates the GUI for Ethan Huang's Baby Names project.

The data used in this project is the Top 1000 baby's name from 1990 to 2010
collected from http://www.ssa.gov/OACT/babynames.

Each name shown on the canvas with different color for clarity,
and will appear as '*' if the rank is below 1000.

"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # To determine the width of each column
    column_width = int((width - GRAPH_MARGIN_SIZE * 2) / len(YEARS))

    return GRAPH_MARGIN_SIZE + column_width * year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Create horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # To create columns
    for i in range(len(YEARS)):
        # To create vertical lines
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)

        # To create the year label for each column
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    vertical_scale = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000
    vertical_start = GRAPH_MARGIN_SIZE

    # For each name in the search box
    for i in range(len(lookup_names)):

        rank_position_list = []  # Store the y position of each year
        rank_list = []  # Store the actual rank of each year

        # To note down whether the name is in the ranking for each year
        # To generate the y position of the dot of the rank in each year

        # The index of the lists below matches the index of YEARS(lst)
        for y in range(len(YEARS)):

            if str(YEARS[y]) in name_data[lookup_names[i]]:
                rank = int(name_data[lookup_names[i]][str(YEARS[y])])
                rank_y = vertical_start + int(vertical_scale * rank)
                rank = str(rank)
            else:
                # The y position will be on horizontal line on the bottom of the canvas
                # And the rank will be replaced with '*'
                rank_y = vertical_start + int(vertical_scale * 1000)
                rank = '*'

            # Add into the lists
            # The index of the lists below matches the index of YEARS(lst)
            rank_position_list.append(rank_y)  # int
            rank_list.append(rank)  # str

        # To draw 11(12-1) lines to combine the dots of each year on the canvas
        for j in range(len(YEARS)-1):

            # Create the start point to the end point of each line
            first_dot_y = rank_position_list[j]
            second_dot_y = rank_position_list[j+1]

            # To determine the color of the line and the text label
            color = COLORS[i % 4]

            # Create the line
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), first_dot_y,
                               get_x_coordinate(CANVAS_WIDTH, j+1), second_dot_y,
                               width=LINE_WIDTH, fill=color)

            # Create the text label
            text_label = str(lookup_names[i]) + ' ' + str(rank_list[j])
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j)+TEXT_DX,
                               first_dot_y,
                               text=text_label, anchor=tkinter.SW, fill=color)

            # If detected the line is the last one
            if j == len(YEARS)-2:
                # Add the text label for the last dot
                text_label = str(lookup_names[i]) + ' ' + str(rank_list[j+1])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1) + TEXT_DX,
                                   second_dot_y,
                                   text=text_label, anchor=tkinter.SW, fill=color)


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
