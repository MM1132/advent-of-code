import math

def solve():
	with open("test.txt") as f:
		numbers = list(map(int, f.readlines()[0]))

	print(numbers)

	counter_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for index, number in enumerate(numbers):
		match_index = index + len(numbers) // 2
		if index + match_index >= len(numbers):
			match_index -= len(numbers)
		if number == numbers[match_index]:
			counter_list[number - 1] += 1

	print(counter_list)

	sum = 0
	for i in range(9):
		sum += (i + 1) * counter_list[i]
	print(sum)

if __name__ == "__main__":
	solve()
