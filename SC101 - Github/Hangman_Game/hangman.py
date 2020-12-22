"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""

import random

# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """

    """
    turns = N_TURNS
    # The chances that the user left.
    the_word = random_word()
    # The answer of the game.
    dashed_word = word(the_word)
    print('The word looks like: ' + dashed_word)
    print('You have ' + str(turns) + ' guesses left.')
    hangman(turns)
    while '-' in dashed_word and turns != 0:
        # The game is not finished yet, keep looping.
        input_ch = str(input('Your guess: '))
        while len(input_ch) > 1 or not input_ch.isalpha():
            # The input is illegal format.
            print('illegal format.')
            hangman(turns)
            input_ch = str(input('Your guess: '))
        input_ch = input_ch.upper()
        # Case-insensitive
        if input_ch not in the_word:
            # The character is not in the word.
            print('There is no ' + str(input_ch) + "'s in the word.")
            turns -= 1
            if turns == 0:
                # The user have used all the chances.
                hangman(turns)
                print('You are completely hung :( ')
                print('The word was: ' + str(the_word))
            else:
                # The user still have chance(s).
                print('The word looks like: ' + dashed_word)
                print('You have ' + str(turns) + ' guesses left.')
                hangman(turns)
        else:
            # The character is in the word.
            ch_number = the_word.find(input_ch)
            dashed_word = new_dashed_word(ch_number, dashed_word, the_word)
            while check(the_word, input_ch, ch_number) != -1:
                # The character appears more than one time in the word, keep finding other indexes.
                ch_number = check(the_word, input_ch, ch_number)
                dashed_word = new_dashed_word(ch_number, dashed_word, the_word)
            if '-' in dashed_word:
                # The game is not finished yet.
                print('You are correct!')
                print('The word looks like: ' + dashed_word)
                print('You have ' + str(turns) + ' guesses left.')
                hangman(turns)
            else:
                # The game is finished, the user win.
                print('You win!!')
                print('The word was: ' + str(the_word))


def check(a, b, c):
    """
    This function checks if the character appears more than one time in the word.
    :param a: str, the word
    :param b: str, the character user input
    :param c: int, the character's index in the word
    :return:
    """
    ans = ''
    ans += a[c + 1:]
    if ans.find(b) == -1:
        return -1
    else:
        num = ans.find(b) + c + 1
        return num


def new_dashed_word(a, b, c):
    """
    This function compose th new dashed_word after user guessed the correct characters.
    :param a: int, the index of the correct character in the_word.
    :param b: str, representing dashed_word
    :param c: str, representing the_word
    :return: str, the new dashed word.
    """
    ans = ''
    ans += b[:a]
    ans += c[a]
    ans += b[a + 1:]
    return ans


def word(a):
    """
    This function turns the_word into dashed-word.
    :param a: str, a random word chose from the function random_word()
    :return: str, the random word as a dashed word.
    """
    ans = ''
    for i in range(len(a)):
        ans += '-'
    return ans


def hangman(a):
    """
    This function will print the hangman.
    :param a: int, turns
    """
    if a == 6:
        print(' ＿＿＿＿\n｜     ｜\n｜\n｜\n｜\n｜\n＿＿＿＿＿＿')
    elif a == 5:
        print(' ＿＿＿＿\n｜     ｜\n｜    （ ）\n｜\n｜\n｜\n＿＿＿＿＿＿')
    elif a == 4:
        print(' ＿＿＿＿\n｜     ｜\n｜    （ ）\n｜    ~｜\n｜\n｜\n＿＿＿＿＿＿')
    elif a == 3:
        print(' ＿＿＿＿\n｜     ｜\n｜    （ ）\n｜    ~｜~\n｜\n｜\n＿＿＿＿＿＿')
    elif a == 2:
        print(' ＿＿＿＿\n｜     ｜\n｜    （ ）\n｜    ~｜~\n｜     ｜\n｜\n＿＿＿＿＿＿')
    elif a == 1:
        print(' ＿＿＿＿\n｜     ｜\n｜    （ ）\n｜    ~｜~\n｜     ｜\n｜     / \n＿＿＿＿＿＿')
    elif a == 0:
        print(' ＿＿＿＿\n｜     ｜\n｜   （xx）\n｜    ~｜~\n｜     ｜\n｜     /\ \n＿＿＿＿＿＿')
    else:
        print(' ＿＿＿＿\n｜\n｜\n｜\n｜\n｜\n＿＿＿＿＿＿')


def random_word():
    """
    This function chooses a random word as the_word.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
