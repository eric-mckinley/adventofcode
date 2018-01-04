class EnhancementData:
    def __init__(self, info):
        info =info.strip("\n")
        self.input = info[0:info.index("=") -1]
        self.output = info[info.index(">") + 2:len(info)]

    def __str__(self):
        return "EnhancementData: in: [{}], out: [{}]".format(self.input, self.output)

    def 

def runProgram(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    for l in lines:
        print(EnhancementData(l))

def runProgram1(grid):

    for i in range(0,7):
        print(grid)
        grid = enhance_grid(grid)
        print("")
    print(grid)
    
def enhance_grid(lines):
    grid = lines.split("\n")

    gridsize = len(grid)
    if gridsize % 3 == 0:
        nextgrid = list()
        for z in range(0, int(gridsize / 3) * 4):
            nextgrid.append("")

        for y in range(0, gridsize, 3):
            for x in range(0, gridsize, 3):
                group = grid[y][x:x + 3] + "\n" + grid[y + 1][x:x + 3] + "\n" + grid[y + 2][x:x + 3]
                fourxfour = enhance_3x3(group).split("\n")
                for fi in range(0, len(fourxfour)) :
                    nextgrid[(int(y / 3) * 4) + fi] += (fourxfour[fi])
        return "\n".join(nextgrid)

    else:
        nextgrid = list()
        for z in range(0, int(gridsize / 2) * 3):
            nextgrid.append("")

        for y in range(0, gridsize, 2):
            for x in range(0, gridsize, 2):
                group = grid[y][x:x + 2] + "\n" + grid[y + 1][x:x + 2]
                threexthree = enhance_2x2(group).split("\n")
                for ti in range(0, len(threexthree)) :
                    nextgrid[(int(y / 2) * 3) + ti] += (threexthree[ti])
        return "\n".join(nextgrid)

def enhance_2x2(twoxtwo):
    return "aaa\nbbb\nccc"


def enhance_3x3(threexthree):
    return "hhhh\niiii\njjjj\nkkkk"


runProgram("input.txt")
# runProgram("abcd\nefgh\nijkl\nmnop")
# print("ODS")
# runProgram("abcdef\nefghij\nijklmn\nmnopqr\nstuvwx\nyzwx23")
