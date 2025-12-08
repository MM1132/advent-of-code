with open("test.txt") as f:
	lines = f.readlines()

lines[0] = lines[0].replace("S", "|")

lines = [[char for char in line] for line in lines]

# print(lines)

split_counter = 0
for line_i in range(len(lines) - 1):
	for char_i, char in enumerate(lines[line_i]):
		if char == '|':
			# Split
			if lines[line_i + 1][char_i] == '.':
				lines[line_i + 1][char_i] = '|'
			elif lines[line_i + 1][char_i] == '^':
				lines[line_i + 1][char_i - 1] = '|'
				lines[line_i + 1][char_i + 1] = '|'
				split_counter += 1

for line in lines:
	print("".join(line).strip())

# print(split_counter)
