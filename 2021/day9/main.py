import itertools
nums = [[int(j) for j in i.strip()] for i in open("input.txt")]
def getBasin(x, y):
    locations = [[x, y]]
    # Left
    if x != 0 and nums[y][x-1] != 9:
            locations.append([x-1, y])
    # Right
    if x != len((nums[y]))-1 and nums[y][x+1] != 9:
        locations.append([x+1, y])
    # Top
    if y != 0 and nums[y-1][x] != 9:
        locations.append([x, y-1])
    # Bottom
    if y != len(nums)-1 and nums[y+1][x] != 9:
        locations.append([x, y+1])
    
    nums[y][x] = 9
    for i in range(len(locations)):
        if not(locations[i][0] == x and locations[i][1] == y):
            locations += getBasin(locations[i][0], locations[i][1])
    return locations

sizes = []
for i in range(len(nums)):
    for j in range(len(nums[i])):
        if nums[i][j] != 9:
            locations = getBasin(j, i)
            locations.sort()
            uniqueLocations = list(i for i, _ in itertools.groupby(locations))
            sizes.append(len(uniqueLocations))
sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
