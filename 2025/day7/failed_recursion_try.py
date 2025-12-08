with open("test.txt") as f:
	lines = f.readlines()

start_index = lines[0].index("S")
lines[0] = lines[0].replace("S", "|")

lines = [[char for char in line] for line in lines]

def count_paths(line_i, char_i, path_counter):
	# The very last line
	if line_i == len(lines) - 1:
		return path_counter + 1
	# Just move one down
	elif lines[line_i + 1][char_i] == '.':
		return path_counter + count_paths(line_i + 1, char_i, path_counter)
	# Split
	elif lines[line_i + 1][char_i] == '^':
		return \
			count_paths(line_i + 1, char_i - 1, path_counter) + \
			count_paths(line_i + 1, char_i + 1, path_counter)

# count_paths()

print(count_paths(0, start_index, 0))

# for line in lines:
# 	print("".join(line).strip())
