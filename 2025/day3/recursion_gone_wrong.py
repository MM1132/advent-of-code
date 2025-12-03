import math

with open("input.txt") as f:
	lines = f.readlines()
	numberLines = [[int(digit) for digit in line[:-1]] for line in lines]

def recursion(line, digitIndex, composition, biggestNumber):
	previous_composition = composition
	
	currentBiggest = biggestNumber
	for index in range(digitIndex, len(line)):
		new_composition = previous_composition + str(line[index])
		if len(new_composition) == 12:
			if int(new_composition) > currentBiggest:
				currentBiggest = int(new_composition)
				continue
		new_biggest = recursion(line, index + 1, new_composition, currentBiggest)
		if new_biggest > currentBiggest:
			currentBiggest = new_biggest
	return currentBiggest

def calculate_biggest(line):
	print(line, "len is", len(line))
	biggest = int(recursion(line, 0, "", 0))
	print(biggest)
	return biggest

total = 0
for line in numberLines:
	biggest = calculate_biggest(line)

	total += biggest

print(total)
