import sys

with open(sys.argv[1]+'.txt','r') as f:
    txt = f.readline()
    parens2Int = {'(':1,')':-1}
    floor = 0; ct = 0
    while floor != -1:
        floor += parens2Int[txt[ct]]
        ct += 1

print(ct)
