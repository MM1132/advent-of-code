import re

with open("input.txt") as f:
	lines = f.readlines()

def get_line_power(line):
	redMax = max(map(int, re.findall(r'\d+(?=\ red)', line)))
	greenMax = max(map(int, re.findall(r'\d+(?=\ green)', line)))
	blueMax = max(map(int, re.findall(r'\d+(?=\ blue)', line)))

	return redMax * greenMax * blueMax

powerCounter = 0
for lineIndex, line in enumerate(lines):
	linePower = get_line_power(line)

	powerCounter += linePower

print(powerCounter)

