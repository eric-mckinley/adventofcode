with open('input.txt') as f:
    lines = f.readlines()

memoryPosition = 0
moves = 0

while memoryPosition < len(lines):
    instructionMove = int(lines[memoryPosition])
    lines[memoryPosition] = instructionMove + 1
    memoryPosition += instructionMove
    moves += 1

print ("Total moves {}".format(moves))