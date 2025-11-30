with open("input.txt") as f:
	lines = f.readlines()

matrix = [
	[0, 0, 1, 0, 0],
	[0,	2, 3, 4, 0],
	[5, 6, 7, 8, 9],
	[0,	"A", "B", "C", 0],
	[0, 0, "D", 0, 0]
]

pos = [1, 1]

def get_button(button_pos):
	if button_pos[0] < 0 or button_pos[0] > 4 or button_pos[1] < 0 or button_pos[1] > 4:
		return False
	button = matrix[button_pos[1]][button_pos[0]]
	if (button == 0):
		return False
	return button

def change_pos(x, y):
	global pos
	new_pos = [pos[0] + x, pos[1] + y]
	# print(type(new_pos[0]))
	if not get_button(new_pos):
		return
	pos = new_pos

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
	
	current_button = get_button(pos)
	print(current_button, end="")

print()

