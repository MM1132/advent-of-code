import math

with open("input.txt") as f:
	lines = list(f.readlines())

# lines = filter(lambda v: v % 2 == 0, lines)

current = 50

counter = 0

for i in range(5):
	print("ranging over 5", i)

for line in lines:
	side = line[0]
	amount = int(line[1:])

	if side == "R":
		for _ in range(amount):
			current += 1
			# print("going right:", current)
			if current >= 100:
				current -= 100
			if current == 0:
				counter += 1
	elif side == "L":
		for _ in range(amount):
			current -= 1
			# print("going left:", current)
			if current < 0:
				current += 100
			if current == 0:
				counter += 1

print(counter)