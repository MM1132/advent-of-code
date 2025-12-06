with open("input.txt") as f:
	parts = f.read().split("\n\n")
	ranges = [list(map(int, part.strip().split("-"))) for part in parts[0].split("\n")]
	numbers = list(map(int, parts[1].split("\n")))

def is_number_in_any_range(n):
	for r in ranges:
		if n >= r[0] and n <= r[1]:
			return True
	return False

counter = 0
for n in numbers:
	if is_number_in_any_range(n):
		counter += 1

print(counter)
