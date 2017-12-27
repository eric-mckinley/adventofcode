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

runProgram1('flqrgnkx')
runProgram1('ffayrhll')