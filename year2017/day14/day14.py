import sys
sys.path.insert(0, '../day10')
import day10

def runProgram1(code):
    total = 0
    for x in range(0, 128):
        s  = "{}-{}".format(code, x)
        hashed = day10.knothash(s)

        for c in hashed:
            text = "{}".format(bin(int(c, 16)))
            for bc in text:
                if bc == '1': total +=  1

    print("Input {} counted {} '1's".format(code, total))


def runProgram2(code):
    grid = list()
    for x in range(0, 128):
        s  = "{}-{}".format(code, x)
        hashed = day10.knothash(s)

        y = 0
        row = list()
        for c in hashed:
            text = pad("{}".format(bin(int(c, 16))[2:]))
            for bc in text:
                row.append(int(bc))
            y += 4
        grid.append(row)

    total = 0
    for y in range(0, 128):
        for x in range(0, 128):
            if grid[x][y] == 1:
                total += 1
                neutraliseconnected(grid, x, y)
    print("Code {} : counted links {}".format(code, total))

def neutraliseconnected(grid, sx, sy):
    if sx -1 >= 0 and grid[sx -1][sy] == 1:
        grid[sx - 1][sy] = 0
        neutraliseconnected(grid, sx -1, sy)

    if sx + 1 < 128 and grid[sx +1][sy] == 1:
        grid[sx + 1][sy] = 0
        neutraliseconnected(grid, sx +1, sy)

    if sy -1 >= 0 and grid[sx][sy -1] == 1:
        grid[sx][sy -1] = 0
        neutraliseconnected(grid, sx, sy -1)

    if sy + 1 < 128 and grid[sx][sy + 1] == 1:
        grid[sx][sy + 1] = 0
        neutraliseconnected(grid, sx, sy +1)

def pad(value):
    if len(value) == 1:
        return "000{}".format(value)
    elif len(value) == 2:
        return "00{}".format(value)
    elif len(value) == 3:
        return "0{}".format(value)
    else:
        return value
    
runProgram1('flqrgnkx')
runProgram1('ffayrhll')
runProgram2('flqrgnkx')
runProgram2('ffayrhll')