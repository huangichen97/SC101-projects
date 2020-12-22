"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program asks users for a DNA sequence as
a python string that is case-insensitive.
"""


def main():
    """
    The program asks users to input a sequence of dna(case-insensitive),
    and uses the function build_complement() to find the complement strand of the DNA sequence.
    """
    dna = input('DNA: ')
    dna = dna.upper()
    print(build_complement(dna))


def build_complement(dna):
    """
    :param dna: str, a DNA sequence that users inputs.
    :return: str, the complement DNA sequence of dna.
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        if base == 'T':
            ans += 'A'
        if base == 'C':
            ans += 'G'
        if base == 'G':
            ans += 'C'
    return ans



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
