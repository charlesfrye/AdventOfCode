import numpy as np
from matplotlib import pyplot as plt
import sys

def turnOn(block):
    block += 1

def turnOff(block):
    block -= 1
    block[block<0] = 0

def toggle(block):
    block += 2

def parse(line):
    split = line.split(' ')
    if split[0] == 'toggle':
        action = 'toggle'
        coords = split[1:]
    elif split[0] == 'turn':
        action = ' '.join(split[0:2])
        coords = split[2:]
    else:
        raise IOError
    coords = parseCoords(coords)
    return action,coords

def parseCoords(coordStr):
    r = []; c = []
    for i in [0,2]:
        r.append(int(coordStr[i].split(',')[0]))
        c.append(int(coordStr[i].split(',')[1]))

    return (r,c)

lights = np.zeros((1000,1000),dtype=np.int8)

with open(sys.argv[1]) as f:
    while True:
        line = f.readline()
        if line == '':
            break
        action,coords = parse(line)
        block = lights[coords[0][0]:coords[0][1]+1,
                        coords[1][0]:coords[1][1]+1]
        if action == 'toggle':
            toggle(block)
        elif action == 'turn on':
            turnOn(block)
        elif action == 'turn off':
            turnOff(block)
        else:
            raise IOError

print(np.sum(lights))
plt.imshow(lights)
plt.draw()
plt.show()
