import sys

def findPairs(line):
    for idx,char in enumerate(line[:-2]):
        pair = char+line[idx+1]
        if line.find(pair,idx+2) != -1:
            return True
    return False

def findXYX(line):
    for idx,char in enumerate(line[:-2]):
        if char == line[idx+2]:
            return True
    return False

nice = 0

with open(sys.argv[1]) as f:
    while True:
        line = f.readline()
        if line == '':
            break
        if not (findPairs(line) and findXYX(line)):
            continue
        nice += 1 

print(nice)
