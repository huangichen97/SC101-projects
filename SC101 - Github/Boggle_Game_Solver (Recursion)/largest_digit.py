"""
File: largest_digit.py
Name: Ethan Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: a given number
	:return: the largest digit in the given number
	"""
	# To store the largest digit
	largest_digit = 0

	# To transform negative integer into positive integer
	if n < 0:
		n *= -1

	largest_d = finding_helper(n, largest_digit)
	return largest_d


def finding_helper(n, largest_digit):
	if n//10 == 0:
		# Base Case
		if n > largest_digit:
			largest_digit = n
		return largest_digit

	else:
		# Recursive Case

		# The units digit of the number
		ans = n % 10

		if ans > largest_digit:
			largest_digit = ans

		# To pop out the units digit of the number
		n //= 10

		return finding_helper(n, largest_digit)


if __name__ == '__main__':
	main()
