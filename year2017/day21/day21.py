def runProgram(grid):

    for i in range(0,5):
        print(grid)
        grid = enhance_grid(grid)
        print("")
    print(grid)
    
def enhance_grid(lines):
    grid = lines.split("\n")

    gridsize = len(grid)
    if gridsize % 3 == 0:
        nextgrid = list()
        for z in range(0, (gridsize / 3) * 4):
            nextgrid.append("")

        for y in range(0, gridsize, 3):
            for x in range(0, gridsize, 3):
                group = grid[y][x:x + 3] + "\n" + grid[y + 1][x:x + 3] + "\n" + grid[y + 2][x:x + 3]
                fourxfour = enhance_3x3(group).split("\n")
                for fi in range(0, len(fourxfour)) :
                    nextgrid[((y / 3) * 4) + fi] += (fourxfour[fi])
        return "\n".join(nextgrid)

    else:
        nextgrid = list()
        for z in range(0, (gridsize / 2) * 3):
            nextgrid.append("")

        for y in range(0, gridsize, 2):
            for x in range(0, gridsize, 2):
                group = grid[y][x:x + 2] + "\n" + grid[y + 1][x:x + 2]
                threexthree = enhance_2x2(group).split("\n")
                for ti in range(0, len(threexthree)) :
                    nextgrid[((y / 2) * 3) + ti] += (threexthree[ti])
        return "\n".join(nextgrid)

def enhance_2x2(twoxtwo):
    return "aaa\nbbb\nccc"


def enhance_3x3(threexthree):
    return "hhhh\niiii\njjjj\nkkkk"


runProgram("abcd\nefgh\nijkl\nmnop")
# print("ODS")
# runProgram("abcdef\nefghij\nijklmn\nmnopqr\nstuvwx\nyzwx23")
