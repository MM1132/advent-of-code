def countCharMatches(str1, str2):
    counter = 0
    for i in str1:
        for j in str2:
            if i == j:
                counter += 1
                break
    return counter
total = 0
digits = [[[k.strip() for k in j.split(" ") if k != ""] for j in i.split("|") if j != ""] for i in open("input.txt")]
for i in digits:
    examples = ["" for _ in range(10)]
    for j in i[0]:
        if len(j) == 2:
            examples[1] = j
            continue
        if len(j) == 4:
            examples[4] = j
            continue
        if len(j) == 3:
            examples[7] = j
            continue
        if len(j) == 7:
            examples[8] = j
            continue
    for j in i[0]:
        if len(j) == 5:
            # Three, because it has 2 in common with 1
            if countCharMatches(examples[1], j) == 2:
                examples[3] = j
                continue
            # Here you should have only 2 and 5 left
            # From which only five matches with 4 exactly 3 times
            elif countCharMatches(examples[4], j) == 3:
                examples[5] = j
                continue
            # And the last one then has to be 2
            else:
                examples[2] = j
                continue
        # Here are 0, 6, 9
        if len(j) == 6:
            # From which, only 6 matches with 1 exactly 1 time
            if countCharMatches(examples[1], j) == 1:
                examples[6] = j
                continue
            # With 9, four matches exactly 4 times, but with 0 it is 3
            elif countCharMatches(examples[4], j) == 4:
                examples[9] = j
                continue
            # If it matched to nothing else, then it must be a 0
            else:
                examples[0] = j
                continue
    # At the end of the line, decode the number
    number = ""
    for j in i[1]:
        for k in range(10):
            if len(j) == len(examples[k]) and countCharMatches(examples[k], j) == len(j):
                number += str(k)
                break
    total += int(number)
print(total)