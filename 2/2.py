import sys
import operator
import functools

def getWrapRibbon(dims):
    return sum(sorted(dims)[0:2]*2)

def getBowRibbon(dims):
    return functools.reduce(operator.mul,dims,1)

with open(sys.argv[1]) as f:
    totalRibbon = 0
    while True:
        dimString = f.readline()
        if dimString == '':
            break
        dimList = [int(l) for l in dimString.split('x')]
        totalRibbon += getWrapRibbon(dimList)
        totalRibbon += getBowRibbon(dimList)

print(totalRibbon)
