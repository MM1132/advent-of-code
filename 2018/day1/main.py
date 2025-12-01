import math

def solve():
	with open("input.txt") as f:
		numbers = list(map(int, f.readlines()))

	# print(numbers[:-1:])

	result = 0
	old_results = [0]
	counter = 0
	while counter < 10000:
		for number in numbers:
			new_result = result + number
			if new_result in old_results:
				print(new_result)
				return
			
			result = new_result
			old_results.append(result)
		
		counter += 1
	
	# print(result)

if __name__ == "__main__":
	solve()
