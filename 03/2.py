import sys

def readInput(fName):
    with open(fName) as f:
        inp = f.readline()
    return inp[:-1] #remove newline

def makeList(inpStr):
    """technically, it's a set"""
    curPos = (0,0)
    lst = set()
    lst.add(curPos)
    directionDict = {'^':(0,1),
		     'v':(0,-1),
                     '>':(1,0),
                     '<':(-1,0)}
    for char in inpStr:
        delta = directionDict[char]
        #`curPos[delta[0]] += delta[1]
        newPos = (curPos[0]+delta[0],curPos[1]+delta[1])
        lst.add(newPos)
        curPos = newPos
    return lst
        
def checkItTwice(lst):
    return len(lst)

inp = readInput(sys.argv[1])
santaLst = makeList(inp[::2])
roboLst = makeList(inp[1::2])
print(checkItTwice(santaLst.union(roboLst)))
