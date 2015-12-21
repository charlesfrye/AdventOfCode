import sys

def memCount(line):
    line = list(line.strip('"'))
    sz = 0
    while line != []:
        char = line.pop(0)
        sz += 1
        if char == '\\':
            if line == []:
                continue
            nxt = line[0]
            if nxt in ['\\','"']:
                del line[0]
                continue
            elif nxt in ['x']:
                del line[0:3]
    return sz

with open(sys.argv[1],'r') as f:
    codeSize = 0
    memSize = 0
    for line in f:
        codeSize += len(line.strip())
        memSize += memCount(line.strip())

print(codeSize)
print(memSize)
print(codeSize-memSize)


