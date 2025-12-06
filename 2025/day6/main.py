import re
from functools import reduce

with open("input.txt") as f:
	lines = f.readlines()

number_pattern = re.compile(r'\d+')
numbers = [[int(m.group()) for m in number_pattern.finditer(line)] for line in lines[:-1]]

sign_pattern = re.compile(r'\S{1}')
signs = [m.group() for m in sign_pattern.finditer(lines[-1])]

print(numbers)

while len(numbers) > 1:
	for i in range(len(signs)):
		if signs[i] == '+':
			numbers[0][i] += numbers[1][i]
		if signs[i] == '*':
			# print(i)
			numbers[0][i] *= numbers[1][i]
	del numbers[1]
	print(numbers)

total = sum(numbers[0])

print(total)