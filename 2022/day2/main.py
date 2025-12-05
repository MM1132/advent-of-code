with open("input.txt") as f:
	rounds = [line.strip().split(" ") for line in f.readlines()]

	for round in rounds:
		# Need to lose
		if round[1] == "X":
			if round[0] == "A": # Rock
				round[1] = "Z"
			elif round[0] == "B": # Paper
				round[1] = "X"
			elif round[0] == "C": # Scissors
				round[1] = "Y"
		# Need to draw
		elif round[1] == "Y":
			round[1] = round[0]
		# Need to win
		elif round[1] == "Z":
			if round[0] == "A": # Rock
				round[1] = "Y"
			elif round[0] == "B": # Paper
				round[1] = "Z"
			elif round[0] == "C": # Scissors
				round[1] = "X"

		for i, side in enumerate(round):
			if round[i] == "A" or round[i] == "X":
				round[i] = "R"
			if round[i] == "B" or round[i] == "Y":
				round[i] = "P"
			if round[i] == "C" or round[i] == "Z":
				round[i] = "S"

def get_round_score(game):
	roundScore = 0

	if game[1] == "R":
		roundScore += 1
		if game[0] == "S":
			roundScore += 6
	if game[1] == "P":
		roundScore += 2
		if game[0] == "R":
			roundScore += 6
	if game[1] == "S":
		roundScore += 3
		if game[0] == "P":
			roundScore += 6
	
	if game[0] == game[1]:
		roundScore += 3
	
	return roundScore

total = 0
for game in rounds:

	roundScore = get_round_score(game)
	print("roundScore:", roundScore)
	total += roundScore

# Rock, Paper, Scissors
# ABC
# XYZ



print(total)
