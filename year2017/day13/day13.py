class FirewallNode:
    def __init__(self, info):
        info = info.strip('\n').replace(' ','')

        self.index = int(info[0:info.index(':')])
        self.depth = int(info[info.index(':') +1:])

    def __str__(self):
        return "Fire: index: {}, depth: {}".format(self.index, self.depth)

def runProgram1(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    nodelist = list()
    for line in lines:
        firewallNode = FirewallNode(line)
        nodelist.append(firewallNode)

    total = 0
    for node in nodelist:
        if   node.index % ((node.depth -1 ) * 2 )  == 0 :
            total += node.index * node.depth
    print("{} Firewall total = {}".format(inputfile, total))

def runProgram2(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    nodelist = list()
    for line in lines:
        firewallNode = FirewallNode(line)
        nodelist.append(firewallNode)

    securitycaught = True
    waittime = 0
    while securitycaught:

        securitycaught = False
        for node in nodelist:
            if  ( waittime + node.index) % ((node.depth -1 ) * 2 )  == 0 :
                securitycaught = True
        waittime += 1
    print("{} Passed through after waiting {}".format(inputfile, waittime -1))

runProgram1('sample.txt')
runProgram1('input.txt')
runProgram2('sample.txt')
runProgram2('input.txt')
