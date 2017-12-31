def runProgram1(check, size, rotation):
    sequence = list()
    sequence.append(0)
    start = 0

    for x in range(1, size + 1):
        index = (start + rotation) % len(sequence)
        if index == len(sequence):
            sequence.append(x)
            start = len(sequence)
        else:
            sequence.insert(index + 1, x)
            start = index + 1
        for x in range(0, len(sequence)):
            if sequence[x] == check:
                print("After is {} is {}".format(x, sequence[x + 1]))


def identifySequence(check, size, rotation):
    print("IDENTIFYING SEQUENCE")
    sequence = list()
    sequence.append(0)
    start = 0
    lasted = 0
    last = 0

    for x in range(1, size + 1):
        index = (start + rotation) % len(sequence)
        if index == len(sequence):
            sequence.append(x)
            start = len(sequence)
        else:
            sequence.insert(index + 1, x)
            start = index + 1
        for z in range(0, len(sequence)):
            if sequence[z] == check:
                if sequence[z + 1] == last:
                    lasted += 1
                else:
                    print
                    if len(sequence) > 1:
                        print("At sequence size {}, after another {} rotations. last value {}, next value {}".format( len(sequence), lasted + 1, last, sequence[z + 1]))
                    print
                    lasted = 0
                    last = sequence[z + 1]

def recreateSequenceQuicker(rot, size):
    print("RECREATING sequence 1 to {}".format(size))
    sx = 1
    lx = 0
    for x in range(1, size + 1):
        sx = (sx + rot) +1
        if sx >= x: sx = sx % x
        if sx == 0 :
            diff = x - lx
            lx = x
            print("Seqeunce size {} - another {} rotations -> next {}".format(x +1, diff, x))

runProgram1(2017, 2017, 3)
runProgram1(2017, 2017, 348)
print("\n----- Part 1 complete -----\n")

identifySequence(0, 10000, 348)
recreateSequenceQuicker(348, 50 * 1000 * 1000)
print("--------")
