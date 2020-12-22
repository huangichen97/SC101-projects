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

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name in name_data:
        # Name in different years

        if year in name_data[name]:
            # Store the lower rank
            current_rank = (name_data[name][year])
            if int(current_rank) > int(rank):
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank

    else:
        # New name
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    first_line = True

    with open(filename, 'r') as f:
        # To split each line in the file
        for line in f:
            if first_line:
                year = line
                year = year.strip()
                first_line = False
            else:
                info_lst = line.split(',')
                rank = info_lst[0]
                name1 = info_lst[1]
                name2 = info_lst[2]
                rank = rank.strip()
                name1 = name1.strip()
                name2 = name2.strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for i in range(len(filenames)):
        add_file(name_data, filenames[i])

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    matching_names = []
    target = target.lower()
    uppercase_target = ''
    for i in range(len(target)):
        if i == 0:
            uppercase_target += target[i].upper()
        else:
            uppercase_target += target[i]

    for baby_name in name_data:
        if target in baby_name or uppercase_target in baby_name:
            matching_names.append(baby_name)

    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
