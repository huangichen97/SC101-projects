"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""



def main():
    """
    User will input a long DNA sequence(s1) and a short DNA sequence(s2).
    The program will find s2 the best match of sections in s1 by the function best_match(s1, s2).
    And then, print it out on the interpreter.
    """
    long_sequence = str(input('Please give me a DNA sequence to search: '))
    short_sequence = str(input('What DNA sequence would you like to match? '))
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    ans = best_match(long_sequence, short_sequence)
    print('The best match is ' + str(ans))


def best_match(s1, s2):
    """
    :param s1: str, the long DNA sequence.
    :param s2: str, the short DNA sequence.
    :return: The program will find the best match and return it as the best_ans.
    """
    point = 0
    # Point is to score the similarity (how much it matched) to the long sequence.
    highest_point = 0
    # The highest point will be kept in this variable.
    best_ans = ''
    # The match that obtain the highest score.
    for i in range(len(s1) - len(s2) + 1):
        # compare s2 to each section of s1.
        for j in range(len(s2)):
            # compare each letter in s2 to the letter in s1.
            if s2[j] == s1[i+j]:
                # The letter matches.
                point += 1
        if point >= highest_point:
            # A new best match is found.
            highest_point = point
            # The highest score will be replaced.
            best_ans = s1[i:i+(len(s2))]
            # best ans will be shown as a string.
        point = 0
        # point will return to zero after a round.
    return best_ans

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
