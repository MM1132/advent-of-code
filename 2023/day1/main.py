import math
import re

with open("input.txt") as f:
	lines = f.readlines()

def toNumber(n):
	if n.isdigit():
		return n
	else:
		match n:
			case "one":
				return 1
			case "two":
				return 2
			case "three":
				return 3
			case "four":
				return 4
			case "five":
				return 5
			case "six":
				return 6
			case "seven":
				return 7
			case "eight":
				return 8
			case "nine":
				return 9

def getFirstAndLastNumbers(line):
	matches = re.findall("(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)", line)
	if len(matches) == 0:
		return [0, 0]
	first = matches[0]
	last = matches[-1]
	return [toNumber(first), toNumber(last)]

def getLastNumber(line):
	matches = [
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
		"1", "2", "3", "4", "5", "6", "7", "8", "9",
	]
	mostRightIndex = 0
	for v in matches:
		index = line.rfind(v)
		if index > mostRightIndex:
			mostRightIndex = index
	# print("ine line", line, "last index is", mostRightIndex)
	first, _ = getFirstAndLastNumbers(line[mostRightIndex:])
	return first

t = 0
for index, line in enumerate(lines):
	first, _ = getFirstAndLastNumbers(line)
	if first == 0:
		continue

	second = getLastNumber(line)

	new_number = int(str(first) + str(second))
	t += new_number

	print(new_number)

print(t)
