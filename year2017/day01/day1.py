def runProgram(input):
    file = open(input, 'r')
    data = file.read()

    first = data[0]
    last = -1
    total = 0

    for c  in data:
        if c == last :
            total += int(c)
        last = c

    if last == first:
        total += int(last)

    print ("Total is {}".format(total))

runProgram('sample1.txt')
runProgram('sample2.txt')
runProgram('sample3.txt')
runProgram('sample4.txt')
runProgram('input.txt')