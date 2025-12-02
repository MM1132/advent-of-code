import math

with open("input.txt") as f:
	lines = f.readlines()[0].split(",")

def is_valid(n):
	as_str = str(n)
	length = len(as_str)
	# print(as_str, length, as_str[1:])
	left = as_str[:length // 2]
	right = as_str[length // 2:]
	# 466466
	return left != right

def solve(lines):
	result = 0

	for v in lines:
		first, second = v.split("-")
		start = int(first)
		end = int(second)

		while start <= end:
			if not is_valid(start):
				result += start

			start += 1

	print(result)


if __name__ == '__main__':
	solve(lines)
