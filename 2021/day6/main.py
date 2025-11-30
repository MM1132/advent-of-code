def calculateFish(number, daysLeft):
    if daysLeft > number:
        return calculateFish(6, daysLeft - number - 1) + calculateFish(8, daysLeft - number - 1)
    return 1

with open("input.txt") as f:
    for i in f:
        fishes = [int(j) for j in i.split(",")]
        break

totalFishes = 0
for j in range(len(fishes)):
    totalFishes += calculateFish(fishes[j], 80)
print(totalFishes)