class ChainNode:
    def __init__(self, info):
        info = info.strip('\n').replace(' ','')

        self.primary = int(info[0:info.index('<')])
        numbers = info[info.index('>') +1:].strip(' ').split(",")
        self.links = list(map(int, numbers))


def recursenodes(allnodes, networklist, nextnode):

    if nextnode.primary not in networklist:
        networklist.append(nextnode.primary)
        for subnode in nextnode.links:
            recursenodes(allnodes, networklist, getNodeByPrimary(allnodes, subnode))

def getNodeByPrimary(allnodes, primaryvalue):
    for node in allnodes:
        if node.primary == primaryvalue:
            return node

def runProgram1(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    nodelist = list()
    for line in lines:
        chainnode = ChainNode(line)
        nodelist.append(chainnode)
        if chainnode.primary == 0:
            zeronode = chainnode

    zeronodelist = list()
    recursenodes(nodelist, zeronodelist, zeronode)

    print("{} : Found connected nodes {} in list {}".format(inputfile, len(zeronodelist), zeronodelist))


def runProgram2(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()


    nodelist = list()
    for line in lines:
        chainnode = ChainNode(line)
        nodelist.append(chainnode)

    chaincount  = 0
    foundchains = list()
    for node in nodelist:
        anodelist = list()
        recursenodes(nodelist, anodelist, node)
        currentchained = len(foundchains)
        for anode in anodelist:
            if anode not in foundchains:
                foundchains.append(anode)
        if currentchained != len(foundchains):
            chaincount += 1
            print("Chain count now {} for new chain {}".format(chaincount, anodelist))

    print("{} : Found {} separate chains".format(inputfile, chaincount))

runProgram1('sample.txt')
runProgram1('input.txt')
runProgram2('sample.txt')
runProgram2('input.txt')