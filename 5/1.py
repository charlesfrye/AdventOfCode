import sys

naughtyStrs = ['ab','cd','pq','xy']

def findNaughties(line):
    return [found != -1 for found in [line.find(s) for s in naughtyStrs]]

def vowelsIn(line):
    return [line.count(vowel) for vowel in ['a','e','i','o','u']]

def findDouble(line):
    for idx, char in enumerate(line[:-1]):
        if char == line[idx+1]:
            return True
    return False

nice = 0
with open(sys.argv[1]) as f:
    while True:
        line = f.readline()
        if line == '':
            break
        if any(findNaughties(line)):
            continue
        if sum(vowelsIn(line))<3:
            continue
        if not findDouble(line):
            continue
        nice += 1

print(nice)

