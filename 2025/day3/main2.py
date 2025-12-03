import math

with open("input.txt") as f:
	lines = f.readlines()
	numberLines = [[int(digit) for digit in line[:-1]] for line in lines]

total = 0
for line in numberLines:
	found_index = -1

	composition = ""
	for i in range(12):

		if i == 11:
			test_line = line[found_index + 1:]
		else:
			test_line = line[found_index + 1:-11 + i]
		# print("i", i)
		# print("found_index", found_index)
		# print("test_line", test_line)
		biggest = max(test_line)
		# print("biggest", biggest)
		found_index = line.index(biggest, found_index + 1)
		# print("found_index", found_index)
		# print(biggest)
		composition += str(biggest)
		# print()

	biggest_number = int(composition)

	print(biggest_number)

	total += biggest_number

print(total)
