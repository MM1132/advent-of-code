with open("input.txt") as f:
	input = f.read()
groups = [list(map(int, group.split("\n"))) for group in input.split("\n\n")]
sums = [sum(group) for group in groups]
total = 0
for i in range(3):
	largest = max(sums)
	total += largest
	sums.remove(largest)
print(total)