with open("input.txt") as f:
	lines = f.readlines()

pos = [1, 1]

def change_pos(x, y):
	global pos
	new_pos = [pos[0] + x, pos[1] + y]
	if new_pos[0] < 0 or new_pos[0] > 2:
		return
	if new_pos[1] < 0 or new_pos[1] > 2:
		return
	pos = new_pos

def get_current_button():
	match pos:
		case [0, 0]:
			return 1
		case [1, 0]:
			return 2
		case [2, 0]:
			return 3
		
		case [0, 1]:
			return 4
		case [1, 1]:
			return 5
		case [2, 1]:
			return 6
		
		case [0, 2]:
			return 7
		case [1, 2]:
			return 8
		case [2, 2]:
			return 9

for line in lines:
	for instruction in line:
		match instruction:
			case "U":
				change_pos(0, -1)
			case "D":
				change_pos(0, 1)
			case "L":
				change_pos(-1, 0)
			case "R":
				change_pos(1, 0)
	
	current_button = get_current_button()
	print(current_button, end="")

print()

