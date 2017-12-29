import copy

def getMoves(filename):
    with open(filename) as file:
        data = file.read()
    return data.strip('\n').split(",")

def swap(list, x, z):
    xv = list[x]
    list[x] = list[z]
    list[z] = xv


def indexOf(list, value):
    for x in range(0, len(list)):
        if list[x] == value: return x


def shiftBy(letters, shift):
    shifted = copy.copy(letters)
    for x in range(0, len(letters)):
        move = x + shift
        if move >= len(letters): move = move - len(letters)
        shifted[move] = letters[x]
    return shifted


def executeMoves(moves, letters):
    for move in moves:
        if move.startswith('s'):
            letters = shiftBy(letters, int(move[1:]))
        elif move.startswith('x'):
            x = int(move[1:move.index('/')])
            y = int(move[move.index('/') + 1:])
            swap(letters, x, y)
        elif move.startswith('p'):
            a = move[1:move.index('/')]
            b = move[move.index('/') + 1:]
            swap(letters, indexOf(letters, a), indexOf(letters, b))
    return letters

def runProgram1(inputfile, letters):
    moves = getMoves(inputfile)

    letters = executeMoves(moves, letters)
    print("{} finishes in state {}".format(inputfile, "".join(letters)))

def runProgram2(inputfile, letters, iterations):
    moves = getMoves(inputfile)
    originalstate = copy.copy(letters)
    count = 0
    refreshedState = False

    while not refreshedState:
        letters = executeMoves(moves, letters)
        count += 1
        refreshedState = letters == originalstate

    remainingiterations = iterations % count
    for x in range(0, remainingiterations):
        letters = executeMoves(moves, letters)

    print("{} runs {} of {} loops to finish in state {} ".format(inputfile, remainingiterations, iterations, "".join(letters)))

runProgram1('sample.txt', ['a', 'b', 'c', 'd', 'e'])
runProgram1('input.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
runProgram2('sample.txt', ['a', 'b', 'c', 'd', 'e'], 1000 * 1000 * 1000)
runProgram2('input.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'], 1000 * 1000 * 1000)
