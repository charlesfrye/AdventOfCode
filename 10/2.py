import sys
from itertools import groupby

def readaloud(number):
    out = []
    for num,group in groupby(number,lambda x:x):
        out.append(len(list(group)))
        out.append(num)
    return out

number = list(map(int,sys.argv[1]))
for i in range(int(sys.argv[2])):
    print(i)
    number = readaloud(number)

print(len(number))
