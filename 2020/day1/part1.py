with open("input.txt") as f:
	numbers = [int(line) for line in f.readlines()]
for index1 in range(len(numbers)):
	for index2 in range(index1 + 1, len(numbers)):
		if numbers[index1] + numbers[index2] == 2020:
			print(numbers[index1] * numbers[index2])
			break
	else:
		continue
	break
