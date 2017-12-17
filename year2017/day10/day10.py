def createSequence(seqsize):
    sequence = list()
    for x in range(0, seqsize):
        sequence.append(x)
    return sequence


def shuffleArray(array, start, length):
    shortlist = list()

    i = 0

    while i < length:
        index = i + start
        if index < len(array):
            shortlist.append(array[index])
        else:
            newindex = index % len(array)
            shortlist.append(array[newindex])
        i += 1

    reversed(shortlist)

    i = 0
    while i < length:
        index = i + start
        if index < len(array):
            array[index] = shortlist[i]
        else:
            array[index - len(array)] = shortlist[i]
        i += 1
    return array

def revesesublist(biglist, index, length):
    return reverseit(getSubList(biglist, index, length))

def getSubList(biglist, index, length):
    count = 0
    sublist = list()
    while count < length:
        if index >= len(biglist):
            index = index % len(biglist)
        sublist.append(biglist[index])
        count += 1
        index += 1
    return sublist

def reverseit(listin):
    listout = list()
    x = len(listin) -1
    while x >= 0:
        listout.append(listin[x])
        x -= 1
    return listout

def runProgram(input, seqsize):
    file = open(input, 'r')
    data = file.read()

    sequence = createSequence(seqsize)
    moves = data.split(",")
    moves = list(map(int, moves))
    index = 0
    for x in range(0, len(moves)):
        move = moves[x]
        revsublist = revesesublist(sequence, index, move)
        for y  in range(0, len(revsublist)):
            sequence[(index + y) % len(sequence)] = revsublist[y]
        index = index + x + move
    print("Final sequence of {} gives answer {} for sequence {}".format(input, sequence[0] * sequence[1], sequence))

runProgram('sample.txt', 5)
print
runProgram('input.txt', 256)
