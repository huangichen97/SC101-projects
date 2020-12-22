"""
File: anagram.py
Name: Ethan Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

dict_lst = []
ans_lst = []
final_lst = []
start_search = True


def main():
    read_dictionary()

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    # Ask users to enter a word
    to_find_s = input(str('Find anagrams for: '))
    to_find_s = to_find_s.lower()
    if to_find_s == EXIT:
        pass
    else:
        find_anagrams(to_find_s)
        print(len(ans_lst), 'anagrams: ', ans_lst)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split()
            dict_lst.append(line[0])


def find_anagrams(s):
    """
    :param s: The word users type in tpo find anagram
    """
    string_lst = []
    for ch in s:
        string_lst.append(ch)
    find_anagrams_helper(string_lst, [], [])


def find_anagrams_helper(string_lst, current_list, index_lst):
    """
    :param string_lst: The word users type in for anagram
    :param current_list: the string in the searching process
    :param index_lst: The index list for the string list, to separate same characters
    """
    global start_search

    if len(current_list) == len(string_lst):
        # Base Case

        # To transform the current list back to string form
        ans_s = ''
        for i in range(len(current_list)):
            ans_s += current_list[i]

        # To check if the word is in the dictionary
        if ans_s in dict_lst:

            # To check if the word has already been printed
            if ans_s in final_lst:
                pass
            else:
                print('Found: ', ans_s)
                ans_lst.append(ans_s)
                final_lst.append(ans_s)

                # Finished a around of word-print, turn oin start_search again.
                start_search = True

    else:
        # The first time into recursion after a word typed in.
        if start_search:
            print('Searching...')
            start_search = False

        for i in range(len(string_lst)):
            # Choose
            if i not in index_lst:
                current_list.append(string_lst[i])
                index_lst.append(i)

                # Explore
                sub_s = ''
                for j in range(len(current_list)):
                    sub_s += current_list[j]

                if has_prefix(sub_s):
                    find_anagrams_helper(string_lst, current_list, index_lst)

                # Un-choose
                current_list.pop()
                index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: The string transferred from the current_lst
    :return: If the word is in the dictionary
    """

    for word in dict_lst:
        if str(word).startswith(sub_s):
            return True

    return False


if __name__ == '__main__':
    main()
