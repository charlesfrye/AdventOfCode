import sys
from collections import namedtuple

Element = namedtuple('Element',['op','arg1','arg2'])

class Circuit():
    """produce a model circuit by:
    1) parsing input
    2) assigning wirenames to parses
    3) resolving wire values on completion"""

    def __init__(self):
        self.elements = {}
        self._cache = {}
        self.ops = {'NOT': self.NOT,
                    'AND': self.AND,
                    'OR': self.OR,
                    'LSHIFT':self.LSHIFT,
                    'RSHIFT':self.RSHIFT,
                    'ASSIGN':self.ASSIGN
                    }
        self.busWidth = 16

    def parse(self,line):
        line = line.split('->')
        inpStr = line[0].strip()
        destStr = line[1].strip()
        element = self.getElement(inpStr)
        return element,destStr

    def assign(self,element,destStr):
        self.elements[destStr] = element

    def resolve(self,wire):
        if  wire == [] or ((type(wire) is list) and (len(wire) == self.busWidth)):
            return wire
        elif type(wire) is int:
            return self.int2arr(wire)
        if wire in self._cache:
            return self._cache[wire]
        element = self.elements[wire]
        print(wire)
        out = self.ops[element.op](self.resolve(element.arg1),
                                   self.resolve(element.arg2))
        if ((type(out) is list) and (len(out) == self.busWidth)):
            self._cache[wire] = out
        return out


    def getElement(self,inpStr):
        inp = inpStr.split(' ')
        args = []; op = 'ASSIGN'
        while not inp == []:
            token = inp.pop(0)
            if token.isnumeric():
                args.append(int(token))
            elif token in self.ops:
                op = token
            else:
                args.append(token)
        if len(args) == 1:
            args.append([])
        element = Element(op=op,arg1=args[0],arg2=args[1])
        return element

    def computeSig(self,args,op):
        if op == []:
            return args[0]
        else:
            return self.ops[op](args)

    def NOT(self,arg1,_):
        string = arg1
        return [not a for a in string]

    def AND(self,arg1,arg2):
        string1 = arg1
        string2 = arg2
        return [a and b for a,b in zip(string1,string2)]

    def OR(self,arg1,arg2):
        string1 = arg1
        string2 = arg2
        return [a or b for a,b in zip(string1,string2)]

    def LSHIFT(self,arg1,arg2):
        string = arg1
        shift = self.arr2int(arg2)
        return string[shift:]+[False]*shift

    def RSHIFT(self,arg1,arg2):
        string = arg1
        shift = self.arr2int(arg2)
        return [False]*shift+string[:-shift]

    def ASSIGN(self,arg1,_):
        return self.resolve(arg1)

    def int2arr(self,num):
        binaryString = bin(num)[2:].zfill(self.busWidth)
        return [char == '1' for char in binaryString]

    def arr2int(self,arr):
        out = 0
        for ind,elem in enumerate(arr[::-1]):
            out += int(elem)*(2)**ind
        return out

circuit = Circuit()

with open(sys.argv[1]) as f:
    for line in f:
        inp, destination = circuit.parse(line)
        circuit.assign(inp,destination)

print(circuit.arr2int(circuit.resolve(sys.argv[2])))
