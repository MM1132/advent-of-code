with open("input.txt") as f:
	input = f.read()
groups = [list(map(int, group.split("\n"))) for group in input.split("\n\n")]
sums = [sum(group) for group in groups]
max_sum = max(sums)
print(max_sum)