reglist = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

class Instruction:
    def __init__(self, info):
        info = info.strip('\n')
        self.command = info[0:3]
        self.register = info[4:5]
        self.value = info[6:]

    def __str__(self):
        return "Instruction: [{}], reg: [{}], value:[{}]".format(self.command, self.register, self.value)

class Program:
    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions
        self.outqueue = list()
        self.pointer = 0
        self.memory = {}
        self.nomove = 0
        self.sendcount = 0
        self.memory['p'] = id

    def execute(self, inqueue):
        instruction = self.instructions[self.pointer]
        if instruction.command == 'set':
            self.memory[instruction.register] = resolve(self.memory, instruction.value)
            self.pointer += 1
        elif instruction.command == 'add':
            self.memory[instruction.register] = memoryValue(self.memory, instruction.register) + resolve(self.memory, instruction.value)
            self.pointer += 1
        elif instruction.command == 'mul':
            self.memory[instruction.register] = memoryValue(self.memory, instruction.register) * resolve(self.memory, instruction.value)
            self.pointer += 1
        elif instruction.command == 'mod' and resolve(self.memory, instruction.value) != 0:
            self.memory[instruction.register] = memoryValue(self.memory, instruction.register) % resolve(self.memory, instruction.value)
            self.pointer += 1
        elif instruction.command == 'jgz' and resolve(self.memory, instruction.register) > 0:
            self.pointer += resolve(self.memory, instruction.value)
        elif instruction.command == 'snd':
            self.outqueue.append(resolve(self.memory, instruction.register))
            self.sendcount += 1
            self.pointer += 1
        elif instruction.command == 'rcv':
            if len(inqueue) > 0:
                self.memory[instruction.register] = inqueue.pop(0)
                self.pointer += 1
                self.nomove = 0
            else:
                self.nomove += 1
        else:
            self.pointer += 1

    def isBlocked(self):
        # Program hasnt moved for 5 cycles
        return self.nomove > 5


def runProgram1(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    instructions = list()
    for line in lines:
        inst = Instruction(line)
        instructions.append(inst)

    memory = execute(instructions)
    print("Final Memory State: {}".format(memory))

def runProgram2(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    instructions = list()
    for line in lines:
        inst = Instruction(line)
        instructions.append(inst)

    program0 = Program(0, instructions)
    program1 = Program(1, instructions)

    while not program0.isBlocked() or not program1.isBlocked():
        program0.execute(program1.outqueue)
        program1.execute(program0.outqueue)

    print("Program 0 send count: {}, Program 1 send count: {}".format(program0.sendcount, program1.sendcount))


def execute(instructions):
    memory = {}
    pointer = 0
    while pointer < len(instructions):
        instruction = instructions[pointer]
        if instruction.command == 'set':
            memory[instruction.register] = resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'add':
            memory[instruction.register] = memoryValue(memory, instruction.register) + resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'mul':
            memory[instruction.register] = memoryValue(memory, instruction.register) * resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'mod' and resolve(memory, instruction.value) != 0:
            memory[instruction.register] = memoryValue(memory, instruction.register) % resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'jgz' and resolve(memory, instruction.register) > 0:
            pointer += resolve(memory, instruction.value)
        elif instruction.command == 'snd':
            memory['sound'] =  resolve(memory, instruction.register)
            pointer += 1
        elif instruction.command == 'rcv' and resolve(memory, instruction.register) > 0:
            print("Recall sound {}".format(memory['sound']))
            pointer += 1
            return memory
        else:
            pointer += 1

def memoryValue(memory, register):
    if register in memory: return memory[register]
    else : return 0


def resolve(memory, value):
    if value in reglist and value in memory: return memory[value]
    elif value in reglist : return 0
    else: return int(value)

print("Part 1 Example")
runProgram1('sample.txt')
print
print("Part 1")
runProgram1('input.txt')
print
print("Part 2 Example")
runProgram2('sample2.txt')
print
print("Part 2")
runProgram2('input.txt')