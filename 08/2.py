import sys

def encodeCount(line):
    line = list(line[1:-1])
    sz = 6
    while line != []:
        char = line.pop(0)
        sz += 1
        if char == '\\':
            sz += 1
        elif char == '"':
            sz += 1
    return sz

with open(sys.argv[1],'r') as f:
    codeSize = 0
    encodeSize = 0
    for line in f:
        codeSize += len(line.strip())
        encodeSize += encodeCount(line.strip())
        #print(len(line.strip()))
        #print(encodeCount(line.strip()))

print(encodeSize)
print(codeSize)
print(encodeSize-codeSize)


