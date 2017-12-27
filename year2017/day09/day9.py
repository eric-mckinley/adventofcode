def runProgram(input):
    file = open(input, 'r')
    data = file.read()

    datalength = len(data)

    braceopen = 0
    garbageopen = 0
    segcount = 0
    total = 0
    i = 0
    noncancelledgarbage = 0
    while i <  datalength:
        if garbageopen == 0:
            if data[i] == '!':
                i+=1
            elif data[i] == '}' and braceopen > 0:
                braceopen -= 1
                segcount += 1
            elif data[i] == '{':
                braceopen += 1
                total += braceopen
            elif data[i] == '<':
                garbageopen = 1
        else:
            if data[i] == '>':
                garbageopen = 0
            elif data[i] == '!':
                i+=1
            else:
                noncancelledgarbage += 1

        i += 1
    print("{} found segments: {} , total: {}, noncancelled: {}".format(input, segcount, total, noncancelledgarbage))

runProgram('sample1.txt')
runProgram('sample2.txt')
runProgram('sample3.txt')
runProgram('sample4.txt')
runProgram('sample5.txt')
runProgram('sample6.txt')
runProgram('sample7.txt')
runProgram('sample8.txt')
print("--------")
runProgram('sample_score_1.txt')
runProgram('sample_score_2.txt')
runProgram('sample_score_3.txt')
runProgram('sample_score_4.txt')
runProgram('sample_score_5.txt')
runProgram('sample_score_6.txt')
runProgram('sample_score_7.txt')
runProgram('sample_score_8.txt')
print("--------")
runProgram("input.txt")
