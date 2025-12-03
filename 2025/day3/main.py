import math

with open("input.txt") as f:
	lines = f.readlines()
	numberLines = [[int(digit) for digit in line[:-1]] for line in lines]

total = 0
for line in numberLines:
	biggest = 0
	for i1, n1 in enumerate(line[:-1]):
		for i2, n2 in enumerate(line[i1 + 1:]):
			new_value = int(str(n1) + str(n2))
			if int(new_value) > biggest:
				biggest = new_value

	total += biggest

print(total)
