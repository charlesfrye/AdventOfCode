import sys

with open(sys.argv[1]+'.txt','r') as f:
    txt = f.readline()
    up = txt.count('(')
    down = txt.count(')')

print(str(up-down))
