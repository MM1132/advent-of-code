def is_digit(n):
	try:
		int(n)
		return True
	except ValueError:
		return False

with open("input.txt") as f:
	raw = f.read().replace("S", "1").replace(".", "0")

lines = [[char if not char.isnumeric() else int(char) for char in line] for line in raw.strip().split("\n")]

for line_i in range(len(lines) - 1):
	for char_i, char in enumerate(lines[line_i]):
		if is_digit(char):
			if char == 0:
				continue
			if is_digit(lines[line_i + 1][char_i]):
				lines[line_i + 1][char_i] += char
			elif lines[line_i + 1][char_i] == "^":
				lines[line_i + 1][char_i - 1] += char
				lines[line_i + 1][char_i + 1] += char

# for line in lines:
# 	for char in line:
# 		print(char, end="")
# 	print()

counter = 0
for char in lines[-1]:
	if is_digit(char):
		counter += char

print(counter)

