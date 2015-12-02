import sys

def getPaper(dims):
    sides = [dims[i]*dims[i-1] for i in [2,1,0]]
    return sum([2*side for side in sides])+min(sides)

with open(sys.argv[1]) as f:
    totalPaper = 0
    while True:
        dimString = f.readline()
        if dimString == '':
            break
        dimList = [int(l) for l in dimString.split('x')]
        totalPaper += getPaper(dimList)

print(totalPaper)
