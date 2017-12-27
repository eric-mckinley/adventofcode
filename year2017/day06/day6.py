
def sumlist(numberList):
    totalval = 0
    index = 0
    while index < len(numberList):
        totalval += numberList[index]
        index += 1
    if totalval != 112:
        print(totalval)
    return totalval

def getHighestIndex(numberList):
    biggestIndex = 0
    index = 1
    while index < len(numberList):
        if numberList[index] > numberList[biggestIndex]:
            biggestIndex = index
        index += 1
    return biggestIndex

def spreadValues(startindex, numberlist):
    spread = numberlist[startindex]

    numberlist[startindex] = 0
    insertindex = startindex +1
    while spread > 0:
        if insertindex >= len(numberlist) :
            insertindex = insertindex - len(numberlist)
        numberlist[insertindex] = numberlist[insertindex] + 1
        spread -= 1
        insertindex += 1
    return numberlist

def readSingleLine(filename):
    file = open(filename, 'r')
    return file.read()


data = readSingleLine('input.txt')
numbers = data.strip(' ').split(",")
numbers = list(map(int, numbers))

sequences = list()
sequences.append(str(numbers).strip('[]'))

found = False
passes = 0
while not found:
    highindex = getHighestIndex(numbers)
    numbers = spreadValues(highindex, numbers)

    passes += 1
    text = str(numbers).strip('[]')
    if text not in sequences:
        sequences.append(text)
    else:
        found = True
        print("Found at {}".format(passes - sequences.index(text)))

print (passes)
