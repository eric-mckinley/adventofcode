class Instruction:
    def __init__(self, info):
        info = info.strip('\n')
        self.segments = info.split(" ")

    def getMemoryLocation(self):
        return self.segments[0]

    def getValueToAdd(self):
        if self.segments[1] == 'inc':
            return int(self.segments[2])
        else:
            return int(self.segments[2]) * -1

    def getQueryMemoryLocation(self):
        return self.segments[4]

    def getEvaluation(self):
        return self.segments[5] + ' ' + self.segments[6]


def runProgram(inputfile):

    with open(inputfile) as f:
        lines = f.readlines()

    memorymap = {}
    instructions = list()

    for line in lines:
        instruction = Instruction(line)
        instructions.append(instruction)
        memorymap[instruction.getMemoryLocation()] = 0
        memorymap[instruction.getQueryMemoryLocation()] = 0


    largest = -100000000
    for instruction in instructions:
        check = "memorymap['{}'] {}".format(instruction.getQueryMemoryLocation(), instruction.getEvaluation())
        if eval(check):
            memorymap[instruction.getMemoryLocation()] = memorymap[instruction.getMemoryLocation()] + instruction.getValueToAdd()
            if memorymap[instruction.getMemoryLocation()] > largest:
                largest = memorymap[instruction.getMemoryLocation()]

    endlargest = -100000000
    for k, v in memorymap.items():
        if v > endlargest:
            endlargest = v
    print("Largest value in registry: {}".format( endlargest))
    print("Largest ever value in registry: {}".format( largest))


runProgram("sample.txt")
runProgram("input.txt")