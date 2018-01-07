class VirusChecker:
    def __init__(self):
        self.dx = 0
        self.dy = 1
        self.x = 0
        self.y = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def turn_back(self):
        self.dx = -self.dx
        self.dy = -self.dy

    def turn_left(self):
        if self.dx == 0:
            self.dx = -self.dy
            self.dy = 0
        else:
            self.dy = self.dx
            self.dx = 0

    def turn_right(self):
        if self.dx == 0:
            self.dx = self.dy
            self.dy = 0
        else:
            self.dy = -self.dx
            self.dx = 0

def as_x_y(nd):
    return [
        int(nd[0:nd.index("_")]),
        int(nd[nd.index("_") + 1:]),
    ]

def printmap(on_nodes, virus_checker):
    lx = 0
    ly = 0
    hx = 0
    hy = 0

    for key in on_nodes:
        x_y = as_x_y(key)
        if x_y[0] < lx: lx = x_y[0]
        if x_y[0] > hx: hx = x_y[0]
        if x_y[1] < ly: ly = x_y[1]
        if x_y[1] > hy: hy = x_y[1]

    astext = list()
    for y in range(hy + 2, ly - 2, -1):
        s = ""
        for x in range(lx - 2, hx + 2):
            pos = "{}_{}".format(x,y)
            if x == virus_checker.x and y == virus_checker.y: s += "0"
            elif pos in on_nodes: s += "#"
            else: s += "."
        astext.append(s)
    print("\n".join(astext))
    print("")

def load_positions(lines, infection_value ):
    positions = {}
    size = len(lines)
    y = (size /2)
    for l in lines:
        l = l.strip("\n")
        x = -(size / 2)
        for c in l:
            if c == "#": positions["{}_{}".format(x,y)] = infection_value
            x += 1
        y -= 1
    return positions



def runProgram1(inputfile, interations, show_end_map):
    with open(inputfile) as f:
        lines = f.readlines()

    infection_value = 1
    nodes = load_positions(lines, infection_value)
    virus_checker = VirusChecker()

    infection_caused = 0

    for x in range(0, interations):

        pos = "{}_{}".format(virus_checker.x, virus_checker.y)
        if pos in nodes and nodes[pos] == infection_value:
            nodes.pop(pos, None)
            virus_checker.turn_right()
        else:
            nodes[pos] = 1
            virus_checker.turn_left()
            infection_caused += 1
        virus_checker.move()

    print("{} after {} iterations caued {} infections".format(inputfile, interations, infection_caused))
    if show_end_map:
        printmap(nodes, virus_checker)


def runProgram2(inputfile, interations):
    with open(inputfile) as f:
        lines = f.readlines()

    infection_value = 3
    weekened_value = 2
    flagged_value = 1

    nodes = load_positions(lines, infection_value)
    virus_checker = VirusChecker()

    infection_caused = 0

    for x in range(0, interations):

        pos = "{}_{}".format(virus_checker.x, virus_checker.y)
        if pos in nodes and nodes[pos] == infection_value:
            nodes[pos] = flagged_value
            virus_checker.turn_right()
        elif pos in nodes and nodes[pos] == flagged_value:
            nodes.pop(pos, None)
            virus_checker.turn_back()
        elif pos in nodes and nodes[pos] == weekened_value:
            nodes[pos] = infection_value
            infection_caused += 1
        else:
            nodes[pos] = weekened_value
            virus_checker.turn_left()
        virus_checker.move()

    print("{} after {} iterations caued {} infections".format(inputfile, interations, infection_caused))

print("\nPart 1 Sample")
runProgram1("sample.txt", 70, True)
runProgram1("sample.txt", 10000, False)
print("\nPart 1")
runProgram1("input.txt", 10000, False)
print("\nPart 2 Sample")
runProgram2("sample.txt", 100)
runProgram2("sample.txt", 10000000)
print("\nPart 2")
runProgram2("input.txt", 10000000)
