reglist = ['a','b','c','d','e','f','g','h']

class Instruction:
    def __init__(self, info):
        info = info.strip('\n')
        self.command = info[0:3]
        self.register = info[4:5]
        self.value = info[6:]

    def __str__(self):
        return "Instruction: [{}], reg: [{}], value:[{}]".format(self.command, self.register, self.value)

def execute(instructions, memory):
    pointer = 0
    mul_invoke_count = 0
    count = 0
    while pointer < len(instructions):

        instruction = instructions[pointer]
        if instruction.command == 'set':
            memory[instruction.register] = resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'add':
            memory[instruction.register] = memoryValue(memory, instruction.register) + resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'sub':
            memory[instruction.register] = memoryValue(memory, instruction.register) - resolve(memory, instruction.value)
            pointer += 1
        elif instruction.command == 'mul':
            memory[instruction.register] = memoryValue(memory, instruction.register) * resolve(memory, instruction.value)
            pointer += 1
            mul_invoke_count += 1
        elif instruction.command == 'jnz' and resolve(memory, instruction.register) != 0:
            pointer += resolve(memory, instruction.value)
        else:
            pointer += 1
        count += 1
    print("Program executed 'mul' command {} times".format(mul_invoke_count))

def memoryValue(memory, register):
    if register in memory: return memory[register]
    else : return 0


def resolve(memory, value):
    if value in reglist and value in memory: return memory[value]
    elif value in reglist : return 0
    else: return int(value)


def loadInstructions(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    instructions = list()
    for line in lines:
        inst = Instruction(line)
        instructions.append(inst)
    return instructions

def initMemory():
    memory = {}
    memory['a'] = 0
    memory['b'] = 0
    memory['c'] = 0
    memory['d'] = 0
    memory['e'] = 0
    memory['f'] = 0
    memory['g'] = 0
    memory['h'] = 0
    return memory

def runProgram1(inputfile):
    instructions =loadInstructions(inputfile)
    memory = initMemory()
    execute(instructions, memory)
    
def runProgram2(inputfile):
    instructions =loadInstructions(inputfile)
    memory = initMemory()
    memory['a'] = 1
    execute(instructions, memory)

runProgram1("input.txt")
# runProgram2("input.txt")