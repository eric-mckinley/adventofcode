def createSequence(seqsize):
    sequence = list()
    for x in range(0, seqsize):
        sequence.append(x)
    return sequence

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

def toSuffixAsciiList(text):
    asciilist = list()
    for c in text:
        asciilist.append(ord(c))
    asciilist.append(17)
    asciilist.append(31)
    asciilist.append(73)
    asciilist.append(47)
    asciilist.append(23)
    return asciilist


def shuffleSequence(sequence, moves, shuffles):
    index = 0
    skip =0
    while shuffles > 0:
        x = 0
        while  x  < len(moves):
            move = moves[x]
            revsublist = revesesublist(sequence, index, move)
            for y  in range(0, len(revsublist)):
                sequence[(index + y) % len(sequence)] = revsublist[y]
            index = index + skip + move
            x += 1
            skip += 1

        shuffles -= 1
    return sequence

def xorlist(list):
    result = list[0]
    for x in range(1, len(list)):
        result = result ^ list[x]
    return result

def toHexString(value):
    hexy =  hex(value)[2:]
    if len(hexy) == 1:
        return "0{}".format(hexy)
    else:
        return hexy

def runProgram1(input, seqsize):

    file = open(input, 'r')
    data = file.read()

    sequence = createSequence(seqsize)
    moves = data.split(",")
    moves = list(map(int, moves))

    sequence = shuffleSequence(sequence, moves, 1)
    print("Final sequence of {} gives answer {} for sequence {}".format(input, sequence[0] * sequence[1], sequence))

def knothash(text):
    asciilist = toSuffixAsciiList(text)

    sequence = createSequence(256)

    sparsehash = shuffleSequence(sequence, asciilist, 64)

    hexlist = list()
    x = 0
    while x + 16 <= len(sparsehash) :
        sublist = getSubList(sparsehash, x, 16)
        hexlist.append(toHexString(xorlist(sublist)))
        x += 16

    hexstr =''.join(str(e) for e in hexlist)
    return hexstr

def runProgram2(input):
    file = open(input, 'r')
    data = file.read()
    hexstr = knothash(data)
    print("{} represented as hash: {}".format(input, hexstr))

def runall():
    print("Part1 Sample")
    runProgram1('sample.txt', 5)
    print
    print("Part1 Main")
    runProgram1('input.txt', 256)
    print
    print("Part2 Main")
    runProgram2('part2_sample_1.txt')
    runProgram2('part2_sample_2.txt')
    runProgram2('part2_sample_3.txt')
    runProgram2('part2_sample_4.txt')
    runProgram2('input.txt')

# Commented out because imported into Day14
# runall()