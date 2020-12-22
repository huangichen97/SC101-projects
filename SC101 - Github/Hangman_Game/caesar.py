"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def main():
    """
    After the user input a magic number,
    this program will generate a new alphabet string,
    and ask the user to input a ciphered string.
    And then, the program will decipher the string
    with the function decipher(a, b) and appear in the interpreter.
    """
    shift = int(input('Secret number: '))
    new_alphabet(shift)
    ciphered_string = input("What's the ciphered string? ")
    ciphered_string = ciphered_string.upper()
    decipher_string = decipher(ciphered_string, new_alphabet(shift))
    print('The deciphered string is: ' + decipher_string)


def new_alphabet(shift):
    """
    :param shift: int, The magic number that user input to produce shifted.
    :return: str, a new_alphabet will be returned.
    """
    first_half = ALPHABET[shift:]
    second_half = ALPHABET[:shift]
    # first_half = ALPHABET[(26 - shift):]
    # second_half = ALPHABET[0:(26 - shift)]
    ans = first_half + second_half
    return ans


def decipher(a, b):
    """
    :param a: str, the ciphered_string that the user type in.
    :param b: str, the new alphabet that have been swifted by the magic number.
    :return: str, the deciphered_string will be returned.
    """
    ans = ''
    length = len(a)
    for i in range(length):
        if a[i] == ' ':
            ans += ' '
        elif a[i] == '!':
            ans += '!'
        elif a[i] == '.':
            ans += '.'
        else:
            decipher_letter = b[ALPHABET.find(a[i])]
            # find the index of a[i] in ALPHABET, and use the index to find letter in new_alphabet.
            ans += decipher_letter
    return ans






#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
