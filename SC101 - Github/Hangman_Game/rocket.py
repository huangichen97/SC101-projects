"""
File: rocket.py
-----------------------
This program will implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.

Adjust the SIZE and build whatever size you want the rocket to be!

"""

SIZE = 3
COL = SIZE * 2


def main():
	"""
	This program will build a rocket with 4 kinds of function,
	and combine them together in the end.
	"""
	build_head()
	build_belt()
	build_upper()
	build_lower()
	build_belt()
	build_head()


def build_head():
	for i in range(SIZE):
		# To keep a space in both sides.
		print(' ', end='')
		for j in range(COL):
			if j < COL/2:
				# left half of the head
				if (i + j) < (SIZE-1):
					print(' ', end='')
				else:
					print('/', end='')
			else:
				# right half of the head
				if (i + COL/2) >= j:
					print('\\', end='')
				else:
					print(' ', end='')
		print('')


def build_belt():
	for i in range(COL+2):
		if i == 0 or i == (COL+1):
			# sides of the rocket
			print('+', end='')
		else:
			print('=', end='')
	print('')


def build_upper():
	for i in range(SIZE):
		for j in range(COL+2):
			if j == 0 or j == (COL + 1):
				# sides of the rocket
				print('|', end='')
			else:
				if (((COL+1)/2)+(i+1)) > j > (((COL+1)/2)-(i+1)):
					# The inner part -- '/\'
					if SIZE % 2 == 1:
						if i % 2 == 0:
							# The row index is EVEN
							if j % 2 == 0:
								# The column index is EVEN
								print('\\', end='')
							else:
								# The column index is ODD
								print('/', end='')
						else:
							# The row index is ODD
							if j % 2 == 0:
								# The column index is EVEN
								print('/', end='')
							else:
								# The column index is ODD
								print('\\', end='')
					else:
						if i % 2 == 0:
							# The row index is EVEN
							if j % 2 == 0:
								# The column index is EVEN
								print('/', end='')
							else:
								# The column index is ODD
								print('\\', end='')
						else:
							# The row index is ODD
							if j % 2 == 0:
								# The column index is EVEN
								print('\\', end='')
							else:
								# The column index is ODD
								print('/', end='')
				else:
					# The outer part -- '.'
					print('.', end='')
		print('')


def build_lower():
	for i in range(SIZE):
		for j in range(COL+2):
			if j == 0 or j == (COL + 1):
				# sides of the rocket
				print('|', end='')
			else:
				if i < j < ((COL + 1) - i):
					# The inner part -- '/\'
					if SIZE % 2 == 1:
						if i % 2 == 1:
							# The row index is ODD
							if j % 2 == 0:
								# The column index is EVEN
								print('\\', end='')
							else:
								# The column index is ODD
								print('/', end='')
						else:
							# The row index is EVEN
							if j % 2 == 0:
								# The column index is EVEN
								print('/', end='')
							else:
								# The column index is ODD
								print('\\', end='')
					else:
						if i % 2 == 1:
							# The row index is ODD
							if j % 2 == 0:
								# The column index is EVEN
								print('\\', end='')
							else:
								# The column index is ODD
								print('/', end='')
						else:
							# The row index is EVEN
							if j % 2 == 0:
								# The column index is EVEN
								print('/', end='')
							else:
								# The column index is ODD
								print('\\', end='')
				else:
					# The outer part -- '.'
					print('.', end='')
		print('')





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()