def runProgram(inputfile,splitter):
    with open(inputfile) as f:
        lines = f.readlines()

    total =0
    for line in lines:
        numbers = line.strip('\n').split(splitter)

        index= 0
        while index < len(numbers):
            numbers[index] = int(numbers[index])
            index += 1
        numbers.sort()
        total += int(numbers[-1]) - int(numbers[0])

    print("Total {}".format(total))

runProgram('sample1.txt', ' ')
runProgram('input.txt', '\t')
