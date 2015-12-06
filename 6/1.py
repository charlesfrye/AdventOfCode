import numpy as np
import sys

def turnOn(block):
    block = np.ones_like(block)

def turnOff(block):
    block = np.zeros_like(block)

def toggle(block):
    block = 1-block

def parse(line):
    split = line.split(' ')
    if split[0] == 'toggle':
        parsed = 'toggle'
        coords = 
    return parsed,block

lights = np.zeros((1000,1000),dtype=int8)

with open(sys.argv[1]) as f:
    while True:
        line = f.readline()
        if line == '':
            break
        parsed,coords = parse(line)
        block = getViewFrom(coords,lights)
        if parsed == 'toggle':
            toggle(block)
        elif parsed == 'turn on':
            turnOn(block)
        elif parsed == 'turn off':
            turnOff(block)


