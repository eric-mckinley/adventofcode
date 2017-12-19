def getMove(direction):
    if direction == 'n':
        return [0, 1]
    elif direction == 'ne':
        return [1, 0]
    elif direction == 'se':
        return [1, -1]
    elif direction == 's':
        return [0, -1]
    elif direction == 'sw':
        return [-1, 0]
    elif direction == 'nw':
        return [-1, 1]
    else:
        raise ValueError('Unexpected direction: {}'.format(direction))


def calcDistance(position):
    ax = 0
    ay = 0
    az = 0

    bx = position[0]
    by = position[1]
    bz = 0 - (bx + by)

    return (abs(ax - bx) + abs(ay - by) + abs(az - bz)) / 2


def runProgram1(input):
    file = open(input, 'r')
    data = file.read()

    directions = data.split(",")
    position = [0, 0]
    for direction in directions:
        move = getMove(direction)
        position[0] = position[0] + move[0]
        position[1] = position[1] + move[1]

    total = calcDistance(position)
    print("Total moves from grid {} is {}".format(position, total))


def runProgram2(input):
    file = open(input, 'r')
    data = file.read()

    maxdistance = 0

    directions = data.split(",")
    position = [0, 0]
    for direction in directions:
        move = getMove(direction)
        position[0] = position[0] + move[0]
        position[1] = position[1] + move[1]
        distance = calcDistance(position)
        if(distance > maxdistance):
            maxdistance = distance

    print("Furthest distance is {}".format(maxdistance))


runProgram1('part1_sample_1.txt')
runProgram1('part1_sample_2.txt')
runProgram1('part1_sample_3.txt')
runProgram1('part1_sample_4.txt')
runProgram1('input.txt')
runProgram2('input.txt')
