class Treenode:
    def __init__(self, info):
        info = info.strip('\n').replace(' ','').replace('->','')
        self.name = info[0:info.index('(')]
        self.weight = int(info[info.index('(') +1:info.index(')')])
        children = info[info.index(')') +1:len(info)]
        self.children = children.split(',')
        self.childrennodes = list()

    def addChildrenNodes(self, allnodes):
        for anode in allnodes:
            if anode.name in self.children:
                self.childrennodes.append(anode)

    def hasChild(self, parentname):
        if parentname in self.children:
            return True
        else:
            return False

    def hasChildren(self):
        return len(self.children) > 0

    def isChildless(self):
        return len(self.children) == 0

    def fullWeight(self):
        totalweight = self.weight
        for childnode in self.childrennodes:
            totalweight += childnode.fullWeight()
        return totalweight

    def outStackWeights(self, pname, depth, gotolevel):
        if depth == gotolevel:
            print("LastParent {} = {}".format(self.name, self.weight))

        print("{} + {} = {} + {}".format(self.name, self.getChildrenNames(), self.weight, self.getChildrenWeights()))

        if depth <= gotolevel:
            for childnode in self.childrennodes:
                # print("{}:[{}] Child {} = {}".format(pname, depth, childnode.name, childnode.fullWeight()))
                childnode.outStackWeights(self.name, depth +1, gotolevel)
            print()

    def getChildrenWeights(self):
        childweights = list()
        for childnode in self.childrennodes:
            childweights.append(childnode.fullWeight())
        return childweights

    def getChildrenNames(self):
        childnames = list()
        for childnode in self.childrennodes:
            childnames.append(childnode.name)
        return childnames

def readlines(filename):
    with open(filename) as f:
        return f.readlines()

def getChildNodes(parentnode, treenodes):
    childnodes = list()
    for childname in parentnode.children:
        for treenode in treenodes:
            if treenode.name == childname:
                childnodes.append(treenode)
    return childnodes

def getNode(nodename, treenodes):
    for treenode in treenodes:
        if treenode.name == nodename:
            return treenode

lines = readlines('input.txt')
treenodes = list()
nodenames = list()

for line in lines:
    nextnode = Treenode(line)
    treenodes.append(nextnode)
    nodenames.append(nextnode.name)


for treenode in treenodes:
    treenode.addChildrenNodes(treenodes)

rootparent = 'notfound'
for nodename in nodenames:
    isparentonly = True
    for treenode in treenodes:
        if treenode.hasChild(nodename):
            isparentonly = False

    if isparentonly:
        rootparent = nodename
        print("ROOT PARENT =  {}".format(rootparent))
        print()


for treenode in treenodes:
    if treenode.name == rootparent:
        i = 0
        while i < 10:
            treenode.outStackWeights('GOD',0, i)
            i += 1
            print("---------")
