with open("input.txt") as nums: crabs = [int(i) for i in nums.read().split(",")]
answers = []
for position in range(1000):
    fuel = 0
    for crab in crabs:
        distance = abs(position - crab)
        fuel += distance * (distance +1) / 2
    answers.append(fuel)
print(min(answers))