import math

with open("input.txt") as f:
	lines = f.readlines()[0].split(",")

def is_valid(n):
	as_str = str(n)
	half_len = len(as_str) // 2
	
	while half_len > 0:
		pattern = as_str[:half_len]

		counter = 0
		while counter < 20:
			if pattern * counter == as_str:
				return False
			counter += 1

		half_len -= 1

	return True

def solve(lines):
	result = 0

	for v in lines:
		first, second = v.split("-")
		start = int(first)
		end = int(second)

		while start <= end:
			if not is_valid(start):
				print(start)
				result += start

			start += 1

	print(result)


if __name__ == '__main__':
	solve(lines)
