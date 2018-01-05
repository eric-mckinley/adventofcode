import datetime

class EnhancementData:
    def __init__(self, in_pattern, out_pattern):
        self.input = in_pattern
        self.output = out_pattern

    def __str__(self):
        return "EnhancementData: in: [{}], out: [{}]".format(self.input, self.output)

def cube_rotations(grid):
    rotations = list()
    rotations.append(grid)
    fgrid = grid
    for x in range(0, 4):
        grid = rotate_block(grid)
        rotations.append(grid)

    grid = mirror_block(fgrid)
    rotations.append(grid)
    for x in range(0, 4):
        grid = rotate_block(grid)
        rotations.append(grid)
    return rotations


def enhance_grid(lines, enhancements):
    grid = lines.split("/")

    gridsize = len(grid)
    if gridsize % 2 == 0:
        nextgrid = list()
        for z in range(0, int(gridsize / 2) * 3):
            nextgrid.append("")

        for y in range(0, gridsize, 2):
            for x in range(0, gridsize, 2):
                group = grid[y][x:x + 2] + "/" + grid[y + 1][x:x + 2]
                threexthree = enhance_pattern(group, enhancements).split("/")
                for ti in range(0, len(threexthree)):
                    nextgrid[(int(y / 2) * 3) + ti] += (threexthree[ti])
        return "/".join(nextgrid)
    else:
        nextgrid = list()
        for z in range(0, int(gridsize / 3) * 4):
            nextgrid.append("")

        for y in range(0, gridsize, 3):
            for x in range(0, gridsize, 3):
                group = grid[y][x:x + 3] + "/" + grid[y + 1][x:x + 3] + "/" + grid[y + 2][x:x + 3]
                fourxfour = enhance_pattern(group, enhancements).split("/")
                for fi in range(0, len(fourxfour)):
                    nextgrid[(int(y / 3) * 4) + fi] += (fourxfour[fi])
        return "/".join(nextgrid)

def enhance_pattern(pattern, enhancements):
    for enhancement in enhancements:
        if pattern == enhancement.input: return enhancement.output
    print("PATTERN NOT FOUND: {}".format(pattern))

def rotate_block(block):
    lines = block.split("/")
    if len(lines) == 3:
        return rotate_3x3_block(lines)
    else:
        return rotate_2x2_block(lines)

def mirror_block(block):
    lines = block.split("/")
    if len(lines) == 3:
        return mirror_3x3_block(lines)
    else:
        return mirror_2x2_block(lines)



def rotate_2x2_block(lines):
    rotated = list()
    rotated.append(lines[1][0:1] + lines[0][0:1])
    rotated.append(lines[1][1:2] + lines[0][1:2])
    return "/".join(rotated)


def rotate_3x3_block(lines):
    rotated = list()
    rotated.append(lines[2][0:1] + lines[1][0:1] + lines[0][0:1])
    rotated.append(lines[2][1:2] + lines[1][1:2] + lines[0][1:2])
    rotated.append(lines[2][2:3] + lines[1][2:3] + lines[0][2:3])
    return "/".join(rotated)


def mirror_2x2_block(lines):
    rotated = list()
    rotated.append(lines[0][1:2] + lines[0][0:1])
    rotated.append(lines[1][1:2] + lines[1][0:1])
    return "/".join(rotated)


def mirror_3x3_block(lines):
    rotated = list()
    rotated.append(lines[0][2:3] + lines[0][1:2] + lines[0][0:1])
    rotated.append(lines[1][2:3] + lines[1][1:2] + lines[1][0:1])
    rotated.append(lines[2][2:3] + lines[2][1:2] + lines[2][0:1])
    return "/".join(rotated)


def runProgram(inputfile, startgrid, rotations):
    with open(inputfile) as f:
        lines = f.readlines()

    enhancements = list()
    for l in lines:

        info = l.strip("\n")
        in_pattern = info[0:info.index("=") - 1]
        out_pattern = info[info.index(">") + 2:len(info)]

        enhdata = EnhancementData(in_pattern, out_pattern)
        enhancements.append(enhdata)
        rotatations = cube_rotations(in_pattern)
        for rotatation in rotatations:
            enhancements.append(EnhancementData(rotatation, out_pattern))

    starttime = datetime.datetime.now()
    for x in range(0, rotations):
        startgrid = enhance_grid(startgrid, enhancements)
    endtime = datetime.datetime.now()
    endgrid = startgrid.replace("/", "\n")

    print("{} rules after {} rotations, ran in {}, gives pixels {}:".format(inputfile, rotations,endtime - starttime, endgrid.count("#")))

firstgrid = ".#./..#/###"
print("Part 1 sample")
runProgram("sample.txt", firstgrid, 2)
print("\nPart 1")
runProgram("input.txt", firstgrid, 5)
print("\nPart 2")
runProgram("input.txt", firstgrid, 18)
