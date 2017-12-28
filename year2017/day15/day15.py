def generate(value, seed):
    next = (seed * value) % 2147483647
    return next

def generatevalues(valuea, seeda, divisor, times):
    values = list()

    for x in range(0, times):
        valuea = generate(valuea, seeda)
        if valuea % divisor == 0: values.append(valuea)
    return values

def last16bin(value):
    s = "{}".format(bin(value))
    return s[len(s) - 16:]


def comparevalues(lista, listb):
    if len(lista) < len(listb):
        max = len(lista)
    else:
        max = len(listb)

    countmatches = 0
    for x in range(0, max):
        if last16bin(lista[x]) == last16bin(listb[x]): countmatches += 1
    return countmatches

def runProgram(id, valuea, seeda, divisora, valueb, seedb, divisorb, times):
    lista = generatevalues(valuea, seeda, divisora, times)
    listb = generatevalues(valueb, seedb, divisorb, times)
    result = comparevalues(lista, listb)
    print("{} values matched {} times".format(id, result))


runProgram("Sample Part1", 65, 16807, 1, 8921, 48271, 1, 1000 * 1000 * 40)
runProgram("Main Part1", 699, 16807, 1, 124, 48271, 1, 1000 * 1000 * 40)
# Notice a mistake, quiz mentions 5 million, but sample still works for 40, as does main
runProgram("Sample Part2", 65, 16807, 4, 8921, 48271, 8, 1000 * 1000 * 40)
runProgram("Main Part2", 699, 16807, 4, 124, 48271, 8, 1000 * 1000 * 40)
