import math

with open("input.txt") as f:
	lines = [[char for char in line.strip()] for line in f.readlines()]
	height = len(lines)
	width = len(lines[0])

def has_roll_at_pos(y, x):
	if x < 0 or y < 0 or x >= width or y >= height:
		return 0
	if lines[y][x] == ".":
		return 0
	return 1

def count_surrounding(y, x):
	c = 0
	c += has_roll_at_pos(y - 1, x - 1)
	c += has_roll_at_pos(y - 1, x)
	c += has_roll_at_pos(y - 1, x + 1)
	c += has_roll_at_pos(y, x + 1)
	c += has_roll_at_pos(y + 1, x + 1)
	c += has_roll_at_pos(y + 1, x)
	c += has_roll_at_pos(y + 1, x - 1)
	c += has_roll_at_pos(y, x - 1)
	return c

counter = 0
while True:
	remove_positions = []
	for y in range(height):
		for x in range(width):
			if lines[y][x] != "@":
				continue

			surrounding_count = count_surrounding(y, x)
			# print("pos", x, y, "has", surrounding_count, "surrounding")
			if surrounding_count < 4:
				counter += 1
				remove_positions.append([x, y])
	
	if len(remove_positions) == 0:
		print("zero positions to be removed")
		break

	for pos in remove_positions:
		for y in range(height):
			for x in range(width):
				if pos[0] == x and pos[1] == y:
					lines[y][x] = "."

print(counter)
