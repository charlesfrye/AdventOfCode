import sys
import numpy as np
from itertools import permutations
from collections import namedtuple


Entry = namedtuple('Entry',['city1','city2','dist'])

class distMaker():

    def __init__(self,numLines):
        self.cities = {}
        numCities = max(np.roots([1,-1,-2*numLines]))
        self.mat = np.zeros((numCities,numCities))

    def add(self,entry):

        if entry.city1 not in self.cities:
            r = len(self.cities)
            self.cities[entry.city1] = r
        else:
            r = self.cities[entry.city1]
        if entry.city2 not in self.cities:
            c = len(self.cities)
            self.cities[entry.city2] = c
        else:
            c = self.cities[entry.city2]

        self.mat[r,c] = entry.dist

def parse(line):
    line = line.split(' ')
    city1 = line[0]
    city2 = line[2]
    dist = int(line[-1])

    return Entry(city1,city2,dist)

def solve_tsp(dist):
    return min( (sum( dist[i] for i in zip(per,per[1:])) ,n,per)
        for n, per in enumerate(i for i in
                    permutations(range(dist.shape[0]),dist.shape[0])) )[0]

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    dist = distMaker(len(lines))
    for line in lines:
        entry = parse(line)
        dist.add(entry)
    dist.mat += dist.mat.T
    print(solve_tsp(dist.mat))
