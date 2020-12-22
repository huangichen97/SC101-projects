"""
File: boggle.py
Name: Ethan Huang
----------------------------------------
TODO: This program creates a boggle game!

The program asks users to input 4 rows to create the boggle grid.
After entering correct input format,
the program starts to find words(with at least 4 letters) that is in the dictionary.

In the process,
the program will print out the word when a word in found,
and will print out the amount of words found in the boggle when finish searching.

Have fun!
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_lst = []
printed_lst = []
illegal = False


def main():
    """
    TODO: The program first read in a dictionary,
    and then ask user to input letters for the boggle game.
    After entering the words,
    the program starts searching for words.

    In the process,
    the program will print out the word when a word in found,
    and will print out the amount of words found in the boggle when finish searching.
    """
    read_dictionary()

    boggle = input_boggle()

    # if the inputs are all correct, the program will start to find words in the boggle
    if not illegal:
        find_word(boggle)
        print('There are', len(printed_lst), 'words in total.')
    else:
        pass


def find_word(boggle):
    """
    :param boggle: The list contains 4 rows(list) of letters
    -------------
    This function label the boggle into (x, y) index as below:
    (0,0) (0,1) (0,2) (0,3)
    (1,0) (1,1) (1,2) (1,3)
    (2,0) (2,1) (2,2) (2,3)
    (3,0) (3,1) (3,2) (3,3)
    """

    # run through all the start point
    for x in range(4):
        for y in range(4):
            # start point = (x, y)
            ch = boggle[x][y]
            cur_word = ch
            used_ch_index = [(x, y)]
            find_word_helper(used_ch_index, cur_word, x, y, boggle)


def find_word_helper(used_ch_index, cur_word, x, y, boggle):
    """
    :param used_ch_index: lst, contains letters used already in the form of index
    :param cur_word: str, current composed word
    :param x: x index of the current point
    :param y: y index of the current point
    :param boggle: The list contains 4 rows(list) of letters
    """
    if not has_prefix(cur_word):
        # Base Case
        return

    else:
        # Recursive Case
        if len(cur_word) == 4 or len(cur_word) > 4:
            # The word consist more than 4 letters
            # To check if the word is in the dictionary
            if cur_word in dict_lst:
                # To check if the word has already been printed
                if cur_word in printed_lst:
                    pass
                else:
                    print('Found: \"' + cur_word + '\"')
                    printed_lst.append(cur_word)

        # No matter the current word is in dict_lst or not
        # the program should keep adding letters and searching
        for i in range(x - 1, x + 2):
            # concludes x-1, x, x+1
            for j in range(y - 1, y + 2):
                # concludes y-1, y, y+1

                if 0 <= i <= 3 and 0 <= j <= 3:
                    # make sure the index is in the boggle

                    # ---- CHOOSE ----
                    if (i, j) not in used_ch_index:
                        # make sure the letter(index) is not used already
                        cur_word += boggle[i][j]
                        used_ch_index.append((i, j))

                        # ---- EXPLORE ----
                        find_word_helper(used_ch_index, cur_word, i, j, boggle)

                        # ---- UN-CHOOSE ----
                        used_ch_index.pop()
                        cur_word = cur_word_pop(cur_word)


def cur_word_pop(cur_word):
    """
    This function pops out the last letter of the word
    ---------------------------------------------------
    :param cur_word: (str) current word
    :return: (str) new word
    """
    ans = ''
    for i in range(len(cur_word) - 1):
        ans += cur_word[i]

    return ans


def input_boggle():
    """
    This function ask user to input 4 random letters for 4 times.

    The program:
    1. checks if the input format is correct
    2. turns input into case-insensitive
    3. append the input into boggle_lst

    :return: (lst) boggle_lst: contains 4 strings (4 rows of letters)
    """
    global illegal
    boggle_lst = []

    for i in range(4):

        row = input(f'{i + 1} row of the letters: ')
        row = row.lower()
        if check_row(row):
            # The input is correct
            row = trans_row(row)
            boggle_lst.append(row)
        else:
            illegal = True
            print('Illegal input')
            break

    return boggle_lst


def check_row(row):
    """
    :param row: str, the user's input
    :return: bool, if the format is correct
    """

    if len(row) != 7:
        return False

    # Check if row[1], row[3], row[5] is space
    for i in range(3):
        if not row[1 + 2 * i].isspace():
            return False

    # Check if row[0], row[2], row[4], row[6] is alpha
    for j in range(4):
        if not row[j * 2].isalpha():
            return False

    return True


def trans_row(row):
    """
    :param row: str, the input includes ' '
    :return: str, letter row without ' '
    """
    ans = []
    for i in range(4):
        ans.append(row[(2 * i)])

    return ans


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split()
            dict_lst.append(line[0])


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dict_lst:
        if str(word).startswith(sub_s):
            return True

    return False


if __name__ == '__main__':
    main()
