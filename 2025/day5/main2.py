with open("input.txt") as f:
	parts = f.read().split("\n\n")
	ranges = [list(map(int, part.strip().split("-"))) for part in parts[0].split("\n")]
	numbers = list(map(int, parts[1].split("\n")))

def are_overlapping(r1, r2):
	return r1[1] >= r2[0] and r2[1] >= r1[0]

# to remove overlaps
r1_i = 0
while r1_i < len(ranges) - 1:
	r2_i = r1_i + 1
	while r2_i < len(ranges):
		if are_overlapping(ranges[r1_i], ranges[r2_i]):
			if ranges[r2_i][0] < ranges[r1_i][0]:
				ranges[r1_i][0] = ranges[r2_i][0]
			if ranges[r2_i][1] > ranges[r1_i][1]:
				ranges[r1_i][1] = ranges[r2_i][1]
			del ranges[r2_i]
			r2_i = r1_i + 1
			continue
		r2_i += 1
	r1_i += 1

print(ranges)

def calculate_ranges_total():
	total = 0
	for r in ranges:
		total += r[1] - r[0] + 1
	return total

total = calculate_ranges_total()

print(total)
