import math

with open("input.txt") as f:
	line = f.readlines()[0]

x, y = 0, 0

instructions = [line for line in line.split(", ")]

dir = "N"
# for v in instructions:
# 	print(v)

visited_locations = [[0, 0]]
def get_reoccuring():
	last_location = visited_locations[-1]
	for location in visited_locations[:-1]:
		if location[0] == last_location[0] and location[1] == last_location[1]:
			return location
	return False

reoccurring = False

for v in instructions:
	side = v[0]
	second = int(v[1:])

	print("Moving by", second, "to", side)

	if side == "R":
		match dir:
			case "N":
				dir = "E"
			case "E":
				dir = "S"
			case "S":
				dir = "W"
			case "W":
				dir = "N"
	elif side == "L":
		match dir:
			case "N":
				dir = "W"
			case "W":
				dir = "S"
			case "S":
				dir = "E"
			case "E":
				dir = "N"
		
	# Move
	match dir:
			case "N":
				# print(y, "changing by", second)
				for _ in range(second):
					y -= 1
					visited_locations.append([x, y])
					reoccurring = get_reoccuring()
					if reoccurring:
						break
				# print("y is now", y)
			case "S":
				for _ in range(second):
					y += 1
					visited_locations.append([x, y])
					reoccurring = get_reoccuring()
					if reoccurring:
						break
			case "E":
				for _ in range(second):
					x += 1
					visited_locations.append([x, y])
					reoccurring = get_reoccuring()
					if reoccurring:
						break
			case "W":
				for _ in range(second):
					x -= 1
					visited_locations.append([x, y])
					reoccurring = get_reoccuring()
					if reoccurring:
						break

	if reoccurring != False:
		break 

# result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print("reoccurring:", reoccurring)
result = abs(x) + abs(y)
print(x, y)
print(result)
