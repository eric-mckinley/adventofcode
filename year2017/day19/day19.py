def runProgram(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()
    for x in range(0, len(lines)):
        lines[x] = lines[x].strip('\n')

    x = lines[0].index('|')
    y = 0
    mx = 0
    my = 1

    letters = list()
    journeylength = 0
    while not (mx == 0 and my == 0) and x >= 0 and y >= 0 and y < len(lines) and x < len(lines[y]):
        moves = move(lines, x, y, mx, my, letters)
        mx = moves[0]
        my = moves[1]
        x += mx
        y += my
        journeylength += 1

    journeylength -= 1 # Subtract last iteration of loop

    letterintersects = "".join(letters)
    print("{} path of {} steps, passes through {}".format(inputfile, journeylength, letterintersects))


def move(lines, x, y, mx, my, letters):
    nextc = lines[y][x]
    if nextc == ' ': return [0,0] #stop if end of the line

    if nextc == '+':
        moves = findNextMove(mx, my, x, y, lines)
        mx = moves[0]
        my = moves[1]
    elif nextc != '|' and nextc != '-':
        letters.append(nextc)
    return [mx, my]

def findNextMove(mx, my, x, y, lines):
    if mx == 0:
        return turnLeftOrRight(x, y, lines)
    else:
        return turnUpOrDown(x, y, lines)

def turnLeftOrRight(x, y, lines):
    if x > 0 and lines[y][x - 1:x] != ' ':
        return [-1, 0]
    elif x + 1 < len(lines[y]) and lines[y][x:x + 1] != ' ':
        return [1, 0]
    else:
        return [0, 0]


def turnUpOrDown(x, y, lines):
    if y > 0 and len(lines[y - 1]) >= x +1  and lines[y - 1][x:x+1] != ' ':
        return [0, -1]
    elif y + 1 < len(lines) and len(lines[y + 1]) >= x +1 and lines[y + 1][x:x +1] != ' ':
        return [0, 1]
    else:
        return [0, 0]

print("Part 1 Example")
runProgram('sample.txt')
print("-------")
print("Part 1 and turns out part 2 also, simples")
runProgram('input.txt')
