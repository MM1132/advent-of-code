lines = []

with open("input.txt") as f:
	lines = f.readlines()

def recursiveFuel(fuel):
	newFuel = int(fuel / 3) - 2
	if (newFuel <= 0):
		return 0
	return newFuel + recursiveFuel(newFuel)

sum = sum([recursiveFuel(int(v)) for v in lines])

print(sum)
