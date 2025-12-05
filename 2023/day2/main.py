import re

with open("input.txt") as f:
	lines = f.readlines()

def is_line_possible(line):
	redPossible = all(n <= 12 for n in map(int, re.findall(r'\d+(?=\ red)', line)))
	greenPossible = all(n <= 13 for n in map(int, re.findall(r'\d+(?=\ green)', line)))
	bluePossible = all(n <= 14 for n in map(int, re.findall(r'\d+(?=\ blue)', line)))

	return redPossible and greenPossible and bluePossible

counter = 0
for lineIndex, line in enumerate(lines):
	linePossible = is_line_possible(line)

	if linePossible:
		gameId = int(re.findall(r'\d+', line)[0])
		# print(gameId)
		counter += gameId

print(counter)

