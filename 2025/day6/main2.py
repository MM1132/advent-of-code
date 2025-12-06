import re
from functools import reduce

with open("input.txt") as f:
	lines = f.readlines()

number_pattern = re.compile(r'\d+')
numbers = [[int(m.group()) for m in number_pattern.finditer(line)] for line in lines[:-1]]

sign_pattern = re.compile(r'\S{1}')
signs = [m.group() for m in sign_pattern.finditer(lines[-1])]


zipped_list = list(zip(*lines[:-1]))[:-1]
columns = [reduce(lambda a, b: a + b, v).strip() for v in zipped_list]
columns.append('')

column_numbers = []
last_added = 0
for c_i, c in enumerate(columns):
	if c == '':
		column_numbers.append(list(map(int, columns[last_added:c_i])))
		last_added = c_i + 1

print(column_numbers)

total = 0
for s_i, s in enumerate(signs):
	if s == '+':
		total += sum(column_numbers[s_i])
	elif s == '*':
		total += reduce(lambda a, b: a * b, column_numbers[s_i])

print(total)
