def removeItems(somelist, element):
    return [i for i in somelist if i != element]

def countX(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

def printBoard(points):
    board = [["." for i in range(10)] for i in range(10)]
    for i in points:
        if board[i[0]][i[1]] == ".":
            board[i[0]][i[1]] = "1"
        elif board[i[0]][i[1]] == "1":
            board[i[0]][i[1]] = "2"
        elif board[i[0]][i[1]] == "2":
            board[i[0]][i[1]] = "3"
    for i in board:
        print(i)

def fromTo(p1, p2):
    if p1[0] < p2[0] and p1[1] < p2[1]:
        r1 = range(p1[0], p2[0]+1)
        r2 = range(p1[1], p2[1]+1)
    elif p1[0] < p2[0] and p1[1] > p2[1]:
        r1 = range(p1[0], p2[0]+1)
        r2 = range(p1[1], p2[1]-1, -1)
    elif p1[0] > p2[0] and p1[1] < p2[1]:
        r1 = range(p2[0], p1[0]+1)
        r2 = range(p2[1], p1[1]-1, -1)
    elif p1[0] > p2[0] and p1[1] > p2[1]:
        r1 = range(p2[0], p1[0]+1)
        r2 = range(p2[1], p1[1]+1)
    
    points = []
    posX = [*r1]
    posY = [*r2]
    for j in range(len(posX)):
        points.append([posX[j], posY[j]])
    return points

lines = [[[int(k.strip()) for k in j.split(",")] for j in i.split("->")] for i in open("input.txt")]
wentThrough = []
for i in lines:
    x1 = i[0][0]
    x2 = i[1][0]
    y1 = i[0][1]
    y2 = i[1][1]
    if x1 == x2:
        if y2 < y1:
            for j in range(y1, y2-1, -1):
                wentThrough.append([x1, j])
        for j in range(y1, y2+1):
            wentThrough.append([x1, j])
    elif y1 == y2:
        if x2 < x1:
            for j in range(x1, x2-1, -1):
                wentThrough.append([j, y1])
        else:
            for j in range(x1, x2+1):
                wentThrough.append([j, y1])
    # The diaggonal part
    else:
        for j in fromTo([x1, y1], [x2, y2]):
            wentThrough.append(j)

overlapCount = len(wentThrough)
totalOverlaps = 0
for i in wentThrough:
    count = countX(wentThrough, i)
    if count > 1:
        totalOverlaps += 1
    wentThrough = removeItems(wentThrough, i)
print(totalOverlaps)